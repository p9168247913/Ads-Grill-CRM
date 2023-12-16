from rest_framework import serializers
from app.models import Users


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('pk','name', 'designation', 'role', 'contact_no', 'pincode', 'email')
        # extra_kwargs = {'password': {'write_only': True}}
