from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Users
from django.http import JsonResponse, HttpResponse
import json
from django.db import transaction

class UsersView(APIView):
    def get(self, request):
        if request.method == 'GET':
            try:
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
                    deleteUser.delete()
            except Users.DoesNotExist:
                return JsonResponse({"message": "Something went wrong! Can't Delete User"}, status=500)
            return JsonResponse({'message': 'User Deleted Successfully'}, status=204)
        
    def put(self, request):
        request_data = json.loads(request.body)
        if not request_data:
            return Response({'message': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
        
        userID = request_data.get('pk')
        userData = request_data.get('data', {})
        name = userData['name']
        designation = userData['designation']
        role = userData['role']
        contact_no = userData['contact_no']
        pincode = userData['pincode']
        email = userData['email']

        if not userID or not userData or not name or not designation or not role or not contact_no or not pincode or not email:
            return Response({'messgae': 'Invalid Credentials'}, status = 400)

        try:
            with transaction.atomic():
                user = Users.objects.get(pk = userID)
                user.name = name
                user.designation = designation
                user.role.name = role
                user.contact_no = contact_no
                user.pincode = pincode
                user.email = email
                user.save()
        except Exception as e:
            return Response({'message': str(e)})
        return Response({'message':'User Updated Successfully'}, status=200)
            

