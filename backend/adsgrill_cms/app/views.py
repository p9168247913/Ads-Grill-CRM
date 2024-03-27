from app.models import Users, Roles
from rest_framework import generics, status
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail
from .serializers import UserCreateSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import SessionAuthentication
from braces.views import CsrfExemptMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import logout
from rest_framework.parsers import MultiPartParser
from django.views import View
from django.db import transaction
import threading

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple

class UserCreateView(CsrfExemptMixin, generics.CreateAPIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserCreateSerializer
    parser_classes = (MultiPartParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        designation = serializer.validated_data['designation']
        if Users.objects.filter(email=email, is_deleted=False):
            return JsonResponse({'message':'User with this email already exists'})
        send_password = serializer.validated_data['password']
        with transaction.atomic():
            self.perform_create(serializer)
        send_email = threading.Thread(target=self.send_login_credentials, args=(serializer.validated_data['email'],send_password, designation))
        send_email.start()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = hashed_password
        super().perform_create(serializer)

    def send_login_credentials(self, username, password, designation):
        subject = ''
        if designation == 'client':
            subject = "Adsgrill crm Client login credentials"
        else:
            subject = "Adsgrill crm login credentials"
        message = f'Your username is: {username} and password is: {password}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [username]

        send_mail(subject,message,from_email, recipient_list)





