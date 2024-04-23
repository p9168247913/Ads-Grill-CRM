from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Users, Roles
from django.http import JsonResponse, HttpResponse
import json
from django.db import transaction
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from braces.views import CsrfExemptMixin


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return
    
class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple

class RolesView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.method == 'GET':
            requestedRoles = list(Roles.objects.all().values())
            return Response({'roles':requestedRoles}, status = 200)
        else:
            return Response({'message': 'Invalid Request Method'}, status = 400)
        
    def post(self, request):
        if request.method == 'POST':
            roleName = request.GET.get('role')
            if not roleName or roleName == None:
                return Response({'message':'Invalid Credentials'}, status = 400 ) 
            try:
                with transaction.atomic():
                    new_Roles = Roles()
                    new_Roles.name = roleName
                    new_Roles.save()
            except Exception as e:
                return Response({'message': str(e)})
        else:
            return Response({'message':'Invalid Request Method'}, status=404)
        return Response({'message':'Role Created Successfully'}, status = 201)