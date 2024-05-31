from app.models import Quotation, QuotationStatus, Nda, About_us, Users, Sale, Desclaimer
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
                QuotationStatus.objects.filter(pk=statusID).update(name=statusName)
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
                return JsonResponse({'message':'Status with this title already exist, please try with another title'}, status=status.HTTP_409_CONFLICT)
            with transaction.atomic():
                Desclaimer.objects.filter(pk=disclaimerID).update(title=title, desc=desc)
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message':'Record updated successfully'}, status=status.HTTP_200_OK)
