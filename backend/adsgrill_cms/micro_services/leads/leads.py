from app.models import Users, Lead, Source, Tag, LeadStatus,Sale
from braces.views import CsrfExemptMixin
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.db.models import ObjectDoesNotExist
from django.db import transaction
import pandas as pd
import json
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django.db.utils import IntegrityError
from os.path import basename
import os
import openpyxl
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple

class LeadView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        parser_classes = (MultiPartParser, FormParser)
        lead_data = request.data
        val = lead_data.get('key')
        if not lead_data or not val:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        if val =='post':
            try:
                with transaction.atomic():            
                    user_instance=request.user
                    source_instance, _ = Source.objects.get_or_create(name=lead_data.get('source'))
                    
                    if lead_data.get('contact_no')==None:
                        return JsonResponse({'message':"Please Enter Contact Details"})

                    # Create Lead instance with related models
                    create_lead = Lead.objects.create(
                        sales_man=user_instance,
                        source=source_instance,
                        client_name=lead_data.get('client_name'),
                        contact_no=lead_data.get('contact_no'),
                        email=lead_data.get('email'),
                        requirement=lead_data.get('requirement')
                    )
                    create_lead.save()
            except IntegrityError as i:
                return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({'message':'Lead Created Successfully'},status=status.HTTP_201_CREATED)
        
        if val == 'bulkUpload':
            parser_class = (FileUploadParser,)
            up_file = request.FILES.get('file')
            upload_folder = 'uploads/leads'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
        
            destination_path = os.path.join(upload_folder, up_file.name)
            with open(destination_path, "wb") as destination:
                for i, chunk in enumerate(up_file.chunks()):
                    destination.write(chunk)
        
            df = pd.read_excel(destination_path, dtype=str)
            df = df.dropna(how='all')
            empty_cols = []
        
            try:
                with transaction.atomic():
                    for ind, row in df.iterrows():
                        xl_sale_man, xl_source, xl_cl_name, xl_email, xl_contact_no, xl_requirement = row
                        xl_cl_name = str(xl_cl_name)
        
                        if pd.isna(xl_contact_no) or not str(xl_contact_no):
                            empty_cols.append('contact_no')
        
                        if empty_cols:
                            col_name = ', '.join(empty_cols)
                            raise Exception(f'Empty fields in columns: {col_name}, Row {ind+2}')
                        else:
                            user_instance = Users.objects.get(email=xl_sale_man.lower())
                            source_instance, _ = Source.objects.get_or_create(name=xl_source)
        
                            create_lead = Lead.objects.create(
                                sales_man=user_instance,
                                source=source_instance,
                                client_name=xl_cl_name,
                                contact_no=xl_contact_no,
                                email=xl_email,
                                requirement=xl_requirement
                            )
                            create_lead.save()
        
            except IntegrityError as i:
                return JsonResponse({'message': str(i)}, status=status.HTTP_400_BAD_REQUEST)
            
            except ObjectDoesNotExist:
                return JsonResponse({'message': f"No Sales Manager Found At Row: {ind+2}"})
        
            except Exception as exc:
                return JsonResponse({'message': str(exc)}, status=400, safe=False)
        
            return JsonResponse({'message': f'{up_file.name} Uploaded Successfully'}, status=status.HTTP_201_CREATED)

    
    def get(self, request):
        try:
            with transaction.atomic():
                allLeads = Lead.objects.filter(is_deleted=False).order_by('-created_at')
                lead_count=allLeads.count()
                assignedLeads=Sale.objects.all().count()
                unassignedLeads=lead_count-assignedLeads
                leads_data = [{
                    'id':lead.pk,
                    'source': lead.source.name,
                    'client_name': lead.client_name,
                    'email': lead.email,
                    'contact_no': lead.contact_no,
                    'requirement':lead.requirement
                } for lead in allLeads]
                
                data = {
                'leads': leads_data,
                'total_leads': lead_count,
                'assigned_leads':assignedLeads,
                'unassigned_leads':unassignedLeads
            }
                return JsonResponse({'lead_data':data}, status=status.HTTP_200_OK)
        except IntegrityError as i:
            return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        parser_classes = (MultiPartParser, FormParser)
        lead_data = request.data
        if not lead_data:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user_instance = Users.objects.get(email=request.user)            
            if user_instance.designation != "sales_manager":
                return JsonResponse({"message":"Sorry! You Can Not edit the lead"})
            
            if lead_data.get('contact_no')==None:
                return JsonResponse({'message':"Please Enter Contact No."})
            
            with transaction.atomic():
                updateLead = Lead.objects.get(pk=lead_data.get('id'))
                source_instance, _ = Source.objects.get_or_create(name=lead_data.get('source'))
                
                updateLead.user = user_instance
                updateLead.source =  source_instance
                updateLead.client_name =  lead_data.get('client_name')
                updateLead.email =  lead_data.get('email')
                updateLead.contact_no=lead_data.get('contact_no')
                updateLead.requirement=lead_data.get('requirement')
                updateLead.save()
                return JsonResponse({'message':'Lead Updated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError as i:
            return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):
        id = request.GET.get('id')
        if not id:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with transaction.atomic():
                deleteLead = Lead.objects.get(pk=id)
                deleteLead.is_deleted = True
                deleteLead.save()
                return JsonResponse({'message':'Lead deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
        except IntegrityError as i:
            return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class LeadInfo(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        val = request.GET.get('key')
        name = request.GET.get('name')
        if not name or not val:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        if val == 'status':
            try:
                with transaction.atomic():
                    leadStatusInstance = LeadStatus.objects.create(name=name)
                    leadStatusInstance.save()
                    return JsonResponse({'message':'Lead Status Created Successfully'}, status=status.HTTP_201_CREATED)
            except IntegrityError as i:
                return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
            
        if val == 'tag':
            try:
                with transaction.atomic():
                    leadTagInstance = Tag.objects.create(name=name)
                    leadTagInstance.save()
                    return JsonResponse({'message':'Lead Tag Created Successfully'}, status=status.HTTP_201_CREATED)
            except IntegrityError as i:
                return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
            
        if val == 'source':
            try: 
                with transaction.atomic():
                    leadSourceInstance = Source.objects.create(name=name)
                    leadSourceInstance.save()
                    return JsonResponse({'message':'Lead Source Created Successfully'}, status=status.HTTP_201_CREATED)
            except IntegrityError as i:
                return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        try:
            allLeadStatus = LeadStatus.objects.all().order_by('-created_at')
            allLeadTags = Tag.objects.all().order_by('-created_at')
            allLeadSource = Source.objects.all().order_by('-created_at')
            leadInfoData = {}

            leadStatus = [{
                'id':status.pk,
                'name':status.name
            } for status in allLeadStatus]

            leadTag = [{
                'id': tag.pk,
                'name': tag.name
            } for tag in allLeadTags]

            leadSource = [{
                'id': source.pk,
                'name': source.name
            } for source in allLeadSource]

            leadInfoData['leadStatus'] = leadStatus
            leadInfoData['leadTag'] = leadTag
            leadInfoData['leadSource'] = leadSource

            return JsonResponse({'leadInfoData':leadInfoData}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        val = request.GET.get('key')
        id = request.GET.get('id')
        if not id or not val:
            return JsonResponse({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        if val == 'status':
            try:
                with transaction.atomic():
                    deleteLeadStatus = LeadStatus.objects.get(pk=id)
                    deleteLeadStatus.delete()
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Lead Status Not Found'}, status=status.HTTP_404_NOT_FOUND)
            except IntegrityError as i:
                return JsonResponse({'message': str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return JsonResponse({'message': 'Lead Status Deleted Successfully'}, status=status.HTTP_200_OK)
            
        if val == 'tag':
            try:
                with transaction.atomic():
                    deleteLeadTag = Tag.objects.get(pk=id)
                    deleteLeadTag.delete()
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Lead Tag Not Found'}, status=status.HTTP_404_NOT_FOUND)
            except IntegrityError as i:
                return JsonResponse({'message': str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return JsonResponse({'message': 'Lead Tag Deleted Successfully'}, status=status.HTTP_200_OK)
            
        if val == 'source':
            try:
                with transaction.atomic():
                    deleteLeadSource = Source.objects.get(pk=id)
                    deleteLeadSource.delete()
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Lead Source Not Found'}, status=status.HTTP_404_NOT_FOUND)
            except IntegrityError as i:
                return JsonResponse({'message': str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return JsonResponse({'message': 'Lead Source Deleted Successfully'}, status=status.HTTP_200_OK)

class LeadExcelDownload(APIView):
    def get(self, request):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws['A1'] = 'Sales Man'
        ws['B1'] = 'Source'
        ws['C1'] = 'Client Name'
        ws['D1'] = 'Email'
        ws['E1'] = 'Contact No'
        ws['F1'] = 'Requirement'
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        wb.save(response)
        return response 


