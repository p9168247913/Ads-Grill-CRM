from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Users
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json

class authLogin(APIView):
    def post(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            try:
                user = Users.objects.get(email=username)
                checkPassword = user.check_password(password)
            except Users.DoesNotExist:
                return JsonResponse({'login':'False', 'status':'Failed', 'message':'User does not exist with this email'})
            if user is not None and checkPassword:
                login(request,user)
                res = JsonResponse({'login':'True', 'status':'Success', 'message':'Authenticated successfully', 'user':{
                    'id':user.pk,
                    'email': user.email,
                    'role':user.role.name,
                    'name': user.name,
                    'contact_no': user.contact_no,
                    'pincode': user.pincode,
                    'designation': user.designation
                }})
                res['token'] = request.session.session_key
                print(res.items())
                return res
            else:
                return JsonResponse({'login':'False', 'status':'Failed', 'message':'Unauthorized, username or password is incorrect'})
            
class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return JsonResponse({'user':{
            'email': '',
            'role': ''
        }, 'message': 'Logout successfully'})
                




