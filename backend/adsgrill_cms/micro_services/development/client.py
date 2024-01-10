from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail
from .serializers import ClientCreateSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout, login
from app.models import Client
import json

class ClientView(generics.CreateAPIView):
    serializer_class = ClientCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        if Client.objects.filter(email=email, is_deleted=False).exists():
            return JsonResponse({'message':'Client with this email already exists'})
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
        subject = "Adsgrill crm client login credentials"
        message = f'Your username is: {username} and password is: {password}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [username]

        send_mail(subject,message,from_email, recipient_list)

    def get(self, request):
        try:
            all_clients = Client.objects.filter(is_deleted=False).order_by("-created_at")
            res_data = [{
                "id":client.pk,
                "name":client.name
            }for client in all_clients]
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'clients':res_data}, status=status.HTTP_200_OK)


class ClientLogin(APIView):
    def post(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            try:
                client = Client.objects.get(email=username)
                checkPassword = client.check_password(password)
            except client.DoesNotExist:
                return JsonResponse({'login':'False', 'status':'Failed', 'message':'User does not exist with this email'})
            if client is not None and checkPassword:
                login(request,client)
                res = JsonResponse({'login':'True', 'status':'Success', 'message':'Authenticated successfully', 'user':{
                    'email': client.email,
                    'name': client.name,
                }})
                res['token'] = request.session.session_key
                return res
            else:
                return JsonResponse({'login':'False', 'status':'Failed', 'message':'Unauthorized, username or password is incorrect'})





