from app.models import Users
from rest_framework import generics, status
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail
from .serializers import UserCreateSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from rest_framework.parsers import MultiPartParser
from django.views import View

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    parser_classes = (MultiPartParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        if Users.objects.filter(email=email, is_deleted=False):
            return JsonResponse({'message':'User with this email already exists'})
        send_password = serializer.validated_data['password']
        self.perform_create(serializer)

        self.send_login_credentials(serializer.validated_data['email'], send_password)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = hashed_password
        super().perform_create(serializer)

    def send_login_credentials(self, username, password):
        subject = "Adsgrill crm login credentials"
        message = f'Your username is: {username} and password is: {password}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [username]

        send_mail(subject,message,from_email, recipient_list)





