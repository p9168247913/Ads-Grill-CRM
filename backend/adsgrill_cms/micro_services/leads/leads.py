from app.models import Users, Lead, Source, Tag, LeadStatus
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.db import transaction
import json
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.utils import IntegrityError
from os.path import basename
import openpyxl

class LeadView(APIView):
    def post(self, request):
        parser_classes = (MultiPartParser, FormParser)
        lead_data = request.data
        if not lead_data:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with transaction.atomic():
                user_instance, _ = Users.objects.get_or_create(pk=lead_data.get('userID'))
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
    
    def get(self, request):
        try:
            with transaction.atomic():
                allLeads = Lead.objects.filter(is_deleted=False).order_by('-created_at')
                leads_data = [{
                    'id':lead.pk,
                    'user':lead.user.name,
                    'source': lead.status.name,
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
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        parser_classes = (MultiPartParser, FormParser)
        lead_data = request.data
        if not lead_data:
            return JsonResponse({'message':'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with transaction.atomic():
                updateLead = Lead.objects.get(pk=lead_data.get('id'))
                user_instance, _ = Users.objects.get_or_create(pk=lead_data.get('userID'))
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
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
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
            
        
            

            


