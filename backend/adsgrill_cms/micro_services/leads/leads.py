from app.models import Users, Lead, Source, Tag, LeadStatus
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

class LeadView(APIView):
    def post(self, request):
        parser_classes = (MultiPartParser, FormParser)
        lead_data = request.data
        val = lead_data.get('key')
        if not lead_data or not val:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        if val =='post':
            try:
                with transaction.atomic():
                    user_instance, _ = Users.objects.get(pk=lead_data.get('userID'))
                    source_instance, _ = Source.objects.get_or_create(name=lead_data.get('source'))
                    tag_instance, _ = Tag.objects.get_or_create(name=lead_data.get('tag'))
                    status_instance, _ = LeadStatus.objects.get_or_create(name=lead_data.get('status'))

                    # Create Lead instance with related models
                    create_lead = Lead.objects.create(
                        user=user_instance,
                        source=source_instance,
                        tag=tag_instance,
                        status=status_instance,
                        client_name=lead_data.get('client_name'),
                        contact_no=lead_data.get('contact_no'),
                        email=lead_data.get('email'),
                        country=lead_data.get('country'),
                        state=lead_data.get('state'),
                        city=lead_data.get('city'),
                        file=lead_data.get('file'),
                    )
                    create_lead.save()
            except IntegrityError as i:
                return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({'message':'Lead Created Successfully'},status=status.HTTP_201_CREATED)
        
        # if val =='bulkUpload':
        #     parser_class = (FileUploadParser,)
        #     up_file = request.FILES.get('file')
        #     upload_folder = 'uploads/leads'
        #     if not os.path.exists(upload_folder):
        #         os.makedirs(upload_folder)
                                                                                                         
        #     destination_path = os.path.join(upload_folder, up_file.name)
        #     with open(destination_path, "wb") as destination:
        #         for i, chunk in enumerate(up_file.chunks()):
        #             destination.write(chunk)
        #     df = pd.read_excel(destination_path)
        #     rowList = df.values.tolist()
        #     empty_cols = []
        #     try:
        #         with transaction.atomic():
        #             for (ind, col) in enumerate(rowList):
        #                 xl_sale_man, xl_source, xl_tag, xl_status, xl_cl_name, xl_email, xl_contact_no, xl_country, xl_state, xl_city = col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9]
        #                 if pd.isna(xl_sale_man):
        #                     empty_cols.append(xl_sale_man)
        #                 if pd.isna(xl_source):
        #                     empty_cols.append(xl_source)
        #                 if pd.isna(xl_tag):
        #                     empty_cols.append(xl_tag)
        #                 if pd.isna(xl_status):
        #                     empty_cols.append(xl_status)
        #                 if pd.isna(xl_cl_name):
        #                     empty_cols.append(xl_cl_name)
        #                 if pd.isna(xl_email):
        #                     empty_cols.append(xl_email)
        #                 if pd.isna(xl_contact_no):
        #                     empty_cols.append(xl_contact_no)
        #                 if pd.isna(xl_country):
        #                     empty_cols.append(xl_country)
        #                 if pd.isna(xl_state):
        #                     empty_cols.append(xl_state)
        #                 if pd.isna(xl_city):
        #                     empty_cols.append(xl_city)
        #         print(empty_cols)

        #     except:
        #         pass        
    
    def get(self, request):
        try:
            with transaction.atomic():
                allLeads = Lead.objects.filter(is_deleted=False).order_by('-created_at')
                leads_data = [{
                    'id':lead.pk,
                    'user':lead.user.name,
                    'source': lead.source.name,
                    'tag': lead.tag.name,
                    'status': lead.status.name,
                    'client_name': lead.client_name,
                    'email': lead.email,
                    'contact_no': lead.contact_no,
                    'country': lead.country,
                    'state': lead.state,
                    'city': lead.city,
                    'file':basename(lead.file.name) if lead.file else None
                } for lead in allLeads]
                return JsonResponse({'leads':leads_data}, status=status.HTTP_200_OK)
        except IntegrityError as i:
            return JsonResponse({'message':str(i)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        parser_classes = (MultiPartParser, FormParser)
        lead_data = request.data
        if not lead_data:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with transaction.atomic():
                updateLead = Lead.objects.get(pk=lead_data.get('id'))
                user_instance, _ = Users.objects.get(pk=lead_data.get('userID'))
                source_instance, _ = Source.objects.get_or_create(name=lead_data.get('source'))
                tag_instance, _ = Tag.objects.get_or_create(name=lead_data.get('tag'))
                status_instance, _ = LeadStatus.objects.get_or_create(name=lead_data.get('status'))
                updateLead.user = user_instance
                updateLead.source =  source_instance
                updateLead.tag =  tag_instance
                updateLead.status =  status_instance

                updateLead.client_name =  lead_data.get('client_name')
                updateLead.email =  lead_data.get('email')
                updateLead.contact_no = lead_data.get('contact_no')
                updateLead.country =  lead_data.get('country')
                updateLead.state =  lead_data.get('state')
                updateLead.city =  lead_data.get('city')
                updateLead.file = lead_data.get('file') if lead_data.get('file') else None
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
        
        
class LeadInfo(APIView):
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
                    return JsonResponse({'message': 'Lead Status Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Lead Status Not Found'}, status=status.HTTP_404_NOT_FOUND)
            except IntegrityError as i:
                return JsonResponse({'message': str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        if val == 'tag':
            try:
                with transaction.atomic():
                    deleteLeadTag = Tag.objects.get(pk=id)
                    deleteLeadTag.delete()
                    return JsonResponse({'message': 'Lead Tag Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Lead Tag Not Found'}, status=status.HTTP_404_NOT_FOUND)
            except IntegrityError as i:
                return JsonResponse({'message': str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        if val == 'source':
            try:
                with transaction.atomic():
                    deleteLeadSource = Source.objects.get(pk=id)
                    deleteLeadSource.delete()
                    return JsonResponse({'message': 'Lead Source Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return JsonResponse({'message': 'Lead Source Not Found'}, status=status.HTTP_404_NOT_FOUND)
            except IntegrityError as i:
                return JsonResponse({'message': str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LeadExcelDownload(APIView):
    def get(self, request):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws['A1'] = 'Sales Manager'
        ws['B1'] = 'Source'
        ws['C1'] = 'Tag'
        ws['D1'] = 'Status'
        ws['E1'] = 'Client Name'
        ws['F1'] = 'Email'
        ws['G1'] = 'Contact_No'
        ws['H1'] = 'Country'
        ws['I1'] = 'State'
        ws['J1'] = 'City'
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        wb.save(response)
        return response 


