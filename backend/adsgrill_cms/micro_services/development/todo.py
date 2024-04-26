from app.models import ToDo
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from braces.views import CsrfExemptMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.db.utils import IntegrityError
from datetime import datetime,timedelta
from django.db.models import Q
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple
    
class TodoView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            requestData = json.loads(request.body)
            desc = requestData.get('desc')
            author = request.user

            ToDo.objects.create(
                description=desc,
                author=author,
            )
        except IntegrityError as i:
            return JsonResponse({"message":str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return JsonResponse({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"Todo item created successfully"}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        try:
            if request.user.role.name == 'admin' or request.user.role.name == 'super-admin':
                to_dos = ToDo.objects.all().order_by('-created_at')
            
            if request.user.role.name == 'sales':
                to_dos = ToDo.objects.filter(author=request.user).order_by('-created_at')
            if to_dos:
                to_do_data = [
                    {
                        'id':todo.pk,
                        'author': todo.author.name,
                        'status': todo.status,
                        'desc':todo.description,
                        'created_at': todo.created_at
                        }
                for todo in to_dos]
            else:
                to_do_data = []
        except Exception as e:
            return JsonResponse({"message":str(e)}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({"todo":to_do_data}, status=status.HTTP_200_OK)
    
    def patch(self, request):
        try:
            requestData = json.loads(request.body)
            id = requestData.get('id')
            todo_instance = ToDo.objects.get(pk=id)
            desc = requestData.get('desc')
            todo_status = requestData.get('status')

            todo_instance.description = desc
            todo_instance.status = todo_status
            todo_instance.save()

        except IntegrityError as i:
            return JsonResponse({"message":str(i)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        except Exception as e:
            return JsonResponse({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"message":"Todo item updated succesfully"}, status=status.HTTP_200_OK)

            