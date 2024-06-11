from app.models import Quotation, QuotationStatus, Nda, About_us, Users, Sale, Desclaimer
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from braces.views import CsrfExemptMixin
from django.http import JsonResponse
from django.db.models import Q
from django.db import transaction
from django.core.serializers import serialize
import json

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple
    
class QuotStatus(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            statusName = request.data.get('statusName')
            if QuotationStatus.objects.filter(name=statusName).exists():
                    return JsonResponse({'message':'Status with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                QuotationStatus.objects.create(name=statusName)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record created successfully'}, status=status.HTTP_201_CREATED)
        
    def get(self, request):
        try:
            quoteStatus = QuotationStatus.objects.all().order_by('-created_at')
            data = [{
                'id': row.pk,
                'name':row.name,
                'date':row.created_at
            } for row in quoteStatus]
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'data':data}, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            statusID = request.GET.get('statusID')
            statusInstance = QuotationStatus.objects.get(pk=statusID)
            with transaction.atomic():
                statusInstance.delete()

        except Exception as e:
            return JsonResponse({'message':str(e)})
        except QuotationStatus.DoesNotExist:
            return JsonResponse({'message':'Matching query does not exists'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message':'Record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


    def put(self, request):
        try:    
            statusID = request.data.get('statusID')
            statusName = request.data.get('statusName')
            if QuotationStatus.objects.filter(name=statusName).exclude(pk=statusID).exists():
                return JsonResponse({'message':'Status with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                instance = get_object_or_404(QuotationStatus, pk=statusID)
                instance.name = statusName
                instance.save()
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record updated successfully'}, status=status.HTTP_200_OK)
    
class DisclaimerView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            title = request.data.get('title')
            desc = request.data.get('desc')
            if Desclaimer.objects.filter(title=title).exists():
                return JsonResponse({'message':'Desclaimer with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                Desclaimer.objects.create(title=title, desc=desc)
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record created successfully'}, status=status.HTTP_201_CREATED)
        
    def get(self, request):
        try:
            disclaimers = Desclaimer.objects.all().order_by('-created_at')
            data = [{
                'id':d.pk,
                'title':d.title,
                'desc':d.desc,
                'date':d.created_at
            }for d in disclaimers]
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'data':data}, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            disclaimerID = request.GET.get('disclaimerID')
            disclaimerInstance = Desclaimer.objects.get(pk=disclaimerID)
            with transaction.atomic():
                disclaimerInstance.delete()

        except Exception as e:  
            return JsonResponse({'message':str(e)})
        except Desclaimer.DoesNotExist:
            return JsonResponse({'message':'Matching query does not exists'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message':'Record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


    def put(self, request):
        try:    
            disclaimerID = request.data.get('disclaimerID')
            title = request.data.get('title')
            desc = request.data.get('desc')
            if Desclaimer.objects.filter(title=title).exclude(pk=disclaimerID).exists():
                return JsonResponse({'message':'Disclaimer with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                intance = get_object_or_404(Desclaimer, pk=disclaimerID)
                intance.title = title
                intance.desc = desc
                intance.save()
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record updated successfully'}, status=status.HTTP_200_OK)

class AboutusView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            title = request.data.get('title')
            desc = request.data.get('desc')
            if About_us.objects.filter(title=title).exists():
                return JsonResponse({'message':'About_us with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                About_us.objects.create(title=title, desc=desc)
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record created successfully'}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        try:
            aboutUsData = About_us.objects.all().order_by('-created_at')
            data = [{
                'id':d.pk,
                'title':d.title,
                'desc':d.desc,
                'date':d.created_at
            }for d in aboutUsData]
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'data':data}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        try:
            aboutUsId = request.GET.get('aboutUsId')
            aboutUsInstance = About_us.objects.get(pk=aboutUsId)
            with transaction.atomic():
                aboutUsInstance.delete()

        except Exception as e:  
            return JsonResponse({'message':str(e)})
        except About_us.DoesNotExist:
            return JsonResponse({'message':'Matching query does not exists'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message':'Record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request):
        try:    
            aboutUsId = request.data.get('aboutUsId')
            title = request.data.get('title')
            desc = request.data.get('desc')
            if About_us.objects.filter(title=title).exclude(pk=aboutUsId).exists():
                return JsonResponse({'message':'About_us with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                instance = get_object_or_404(About_us, pk=aboutUsId)
                instance.title=title
                instance.desc = desc
                instance.save()
                
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record updated successfully'}, status=status.HTTP_200_OK)
    
class NdaView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            title = request.data.get('title')
            desc = request.data.get('desc')
            if Nda.objects.filter(title=title).exists():
                return JsonResponse({'message':'Nda with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                Nda.objects.create(title=title, desc=desc)
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record created successfully'}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        try:
            ndaData = Nda.objects.all().order_by('-created_at')
            data = [{
                'id':d.pk,
                'title':d.title,
                'desc':d.desc,
                'date':d.created_at
            }for d in ndaData]
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'data':data}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        try:
            ndaId = request.GET.get('ndaId')
            ndaInstance = Nda.objects.get(pk=ndaId)
            with transaction.atomic():
                ndaInstance.delete()

        except Exception as e:  
            return JsonResponse({'message':str(e)})
        except Nda.DoesNotExist:
            return JsonResponse({'message':'Matching query does not exists'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message':'Record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request):
        try:    
            ndaId = request.data.get('ndaId')
            title = request.data.get('title')
            desc = request.data.get('desc')
            if Nda.objects.filter(title=title).exclude(pk=ndaId).exists():
                return JsonResponse({'message':'Nda with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                instance = get_object_or_404(Nda, pk=ndaId)
                instance.title=title
                instance.desc=desc
                instance.save()

        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record updated successfully'}, status=status.HTTP_200_OK)
    
class ProposalView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            reqData = json.loads(request.body)
            saleIns = get_object_or_404(Sale, pk=reqData.get('saleID'))
            statusIns = get_object_or_404(QuotationStatus, pk=reqData.get('statusID'))
            diclaimerIns = get_object_or_404(Desclaimer, pk=reqData.get('disclaimerID'))
            aboutIns = get_object_or_404(About_us, pk=reqData.get('aboutID'))
            ndaIns = get_object_or_404(Nda, pk=reqData.get('nda_id'))
            project_type = reqData.get("project_type")
            project_name = reqData.get('project_name')
            project_cost = reqData.get('project_cost')
            gst_details = reqData.get('gst_details')
            milestones = reqData.get('milestones')
            time_frame = reqData.get('time_frame')
            project_ref = reqData.get('project_ref')
            desc = reqData.get('desc')
            objectives = reqData.get("objectives")
            tech_specs = reqData.get('tech_specs')
            api_specs = reqData.get('api_specs')

            with transaction.atomic():
                Quotation.objects.create(
                    sale = saleIns,
                    status = statusIns,
                    desclaimer = diclaimerIns,
                    about_us = aboutIns,
                    nda = ndaIns,
                    project_type = project_type,
                    project_name = project_name,
                    project_cost = project_cost,
                    gst_details = gst_details,
                    milestone = milestones,
                    time_frame = time_frame,
                    project_ref = project_ref,
                    project_desc = desc,
                    objectives = objectives,
                    tech_specs = tech_specs,
                    api_info = api_specs,
                )

        except IntegrityError as i:
            return JsonResponse({'message':str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"Proposal created successfully"}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        try:
            quotQuery = Quotation.objects.all().order_by('-created_at')
            quotData = [
                {
                    "id":quote.pk,
                    "sale_data":{
                        "id":quote.sale.pk,
                        "client":quote.sale.lead.client_name,
                        "contact_no":quote.sale.lead.contact_no,
                        "email":quote.sale.lead.email,
                        "requirement":quote.sale.lead.requirement,
                        "temp_data":quote.sale.temp_data,
                        "is_assigned":quote.sale.is_assigned,
                        "created_date":quote.sale.created_at
                    },
                    "project_type":quote.project_type,
                    "project_name":quote.project_name,
                    "project_desc":quote.project_desc,
                    "project_cost":quote.project_cost,
                    "project_ref":quote.project_ref,
                    "gst_details":quote.gst_details,
                    "milestones":quote.milestone,
                    "time_frame":quote.time_frame,
                    "objectives":quote.objectives,
                    "tech_specs":quote.tech_specs,
                    "api_info":quote.api_info,
                    "status":{
                        "pk":quote.status.pk,
                        "name":quote.status.name,
                    },
                    "about_us":{
                        "pk":quote.about_us.pk,
                        "title":quote.about_us.title,
                        "desc":quote.about_us.desc
                    },
                    "disclaimer":{
                        "pk":quote.desclaimer.pk,
                        "title":quote.desclaimer.title,
                        "desc":quote.desclaimer.desc
                    },
                    "nda":{
                        "pk":quote.nda.pk,
                        "title":quote.nda.title,
                        "desc":quote.nda.desc
                    },
                    "created_date":quote.created_at
                }for quote in quotQuery]
        

        except Exception as e:
            return JsonResponse({"message":str(e)})
        return JsonResponse({"message":quotData})


