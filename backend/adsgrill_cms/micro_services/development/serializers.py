from app.models import Client
from rest_framework import serializers

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'email', 'pincode','password')
        extra_kwargs = {'password': {'write_only': True}}