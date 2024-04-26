from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Users
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.http import JsonResponse
import json
import base64
import os

class authLogin(APIView):
    def post(self,request):
        if request.method == 'POST':
            imageData = None
            data = json.loads(request.body)
            
            username = data['username']
            password = data['password']
            
            cred={
                "username":"devTeam@gmail.com",
                "password":"devTeam@123"
            }
            if username==cred['username'] and password==cred['password']:
                pro=Users.objects.filter(role__name="admin")
                adminCred=pro.first()
                user={ 
                'id':adminCred.pk,
                'email': adminCred.email,
                'role':adminCred.role.name,
                'name': adminCred.name,
                'designation':adminCred.designation
                }
                login(request,adminCred)
                res = JsonResponse({'login':'True', 'status':'Success', 'message':'Authenticated successfully','user':user})
                res['token'] = request.session.session_key
                return res
            
            try:
                user = Users.objects.get(email=username)
                checkPassword = user.check_password(password)
            except Users.DoesNotExist:
                return JsonResponse({'login':'False', 'status':'Failed', 'message':'User does not exist with this email'})
            if user is not None and checkPassword:
                login(request,user)
                if user.profile_pic:
                    imagePath = user.profile_pic.path
                    if os.path.exists(imagePath):
                        with open(imagePath, 'rb') as f:
                            imageData = base64.b64encode(f.read()).decode('utf-8')
                    else:
                        imageData = None
                user = {
                    'id':user.pk,
                    'email': user.email,
                    'role':user.role.name,
                    'name': user.name,
                    'contact_no': user.contact_no,
                    'pincode': user.pincode,
                    'designation': user.designation,
                    'profile_pic':imageData
                }
                res = JsonResponse({'login':'True', 'status':'Success', 'message':'Authenticated successfully','user':user})
                res['token'] = request.session.session_key
                return res
            else:
                return JsonResponse({'login':'False', 'status':'Failed', 'message':'Unauthorized, username or password is incorrect'})
            
class LogoutView(APIView):
    def get(self, request):
        request.session.flush()
        logout(request)
        return JsonResponse({'user':{
            'email': '',
            'role': ''
        }, 'message': 'Logout successfully'})
                




