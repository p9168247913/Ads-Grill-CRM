from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Users
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
import json
from django.db import transaction
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from braces.views import CsrfExemptMixin
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError
import os
import base64

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple

class UsersView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.method == 'GET':
            try:
                user_data = []
                imageData = None
                role = request.GET.get('role')
                requestedUsers = Users.objects.filter(role__name=role, is_deleted=False).order_by('-created_at')
                for user in requestedUsers:
                    if user.profile_pic:
                        imagePath = user.profile_pic.path
                        if os.path.exists(imagePath):
                            with open(imagePath, 'rb') as f:
                                imageData = base64.b64encode(f.read()).decode('utf-8')
                        else:
                            imageData = None
                    User = {
                    'id':user.pk,
                    'name': user.name,
                    'email': user.email,
                    'designation': user.designation,
                    'role': user.role.name,
                    'contact_no': user.contact_no,
                    'pincode': user.pincode,
                    'profile_pic':imageData
                    }
                    user_data.append(User)
            except Users.DoesNotExist:
                return JsonResponse({'Message': 'No users found for this department'}, status=404, safe=False)
        else:
            return JsonResponse({'users': '', 'message': 'Invalid Request Method'}, status=405, safe=False)
        return JsonResponse({'users': user_data})
    
    def delete(self, request):
        if request.method == 'DELETE':
            try:
                with transaction.atomic():
                    userID = request.GET.get('userID')
                    deleteUser = Users.objects.filter(pk = userID)
                    deleteUser.update(is_deleted=True)
            except Users.DoesNotExist:
                return JsonResponse({"message": "Something went wrong! Can't Delete User"}, status=500)
            return JsonResponse({'message': 'User Deleted Successfully'}, status=204)
        
    def put(self, request):
        requestData = request.data
        if not requestData:
            return Response({'message': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)
        
        userID = requestData.get('userID')
        name = requestData.get('name')
        designation = requestData.get('designation')
        role = requestData.get('role')
        contact_no = requestData.get('contact_no')
        pincode = requestData.get('pincode')
        email = requestData.get('email')
        profile_pic = request.FILES.get('profile_pic')
        user = Users.objects.get(pk = userID)

        newPassword = None
        if requestData.get('oldPassword') and requestData.get('newPassword') and requestData.get('confirmPassword'):
            if check_password(requestData.get('oldPassword'), request.user.password):
                newPassword = make_password(requestData.get('newPassword'))
            else:
                return JsonResponse({"detail":"The old password you provided is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                user.name = name
                user.designation = designation
                user.role.name = role
                user.contact_no = contact_no
                user.pincode = pincode
                user.email = email
                if newPassword:
                    user.password = newPassword
                if profile_pic:
                    user.profile_pic = profile_pic
                user.save()
        except IndentationError as i:
            return Response({'message': str(i)})
        except Exception as e:
            return Response({'message': str(e)})
        return Response({'message':'User Updated Successfully'}, status=200)
            

