from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Users
from django.http import JsonResponse
import json

class UsersView(APIView):
    def get(self, request):
        if request.method == 'GET':
            role = request.GET.get('role')
            requestedUsers = Users.objects.filter(role__name=role)
            user_data = [{
                'name': user.name,
                'designation': user.designation,
                'role': user.role.name,
                'contact_no': user.contact_no,
                'pincode': user.pincode,
                # 'pro_pic': user.profile_pic
            } for user in requestedUsers]
            return JsonResponse({'users': user_data})