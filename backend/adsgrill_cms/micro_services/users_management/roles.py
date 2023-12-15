from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Users, Roles
from django.http import JsonResponse, HttpResponse
import json
from django.db import transaction

class RolesView(APIView):
    def get(self, request):
        if request.method == 'GET':
            requestedRoles = list(Roles.objects.all().values())
            return Response({'roles':requestedRoles}, status = 200)
        else:
            return Response({'message': 'Invalid Request Method'}, status = 400)
        
    def post(self, request):
        if request.method == 'POST':
            roleName = request.GET.get('role')
            print(roleName)
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