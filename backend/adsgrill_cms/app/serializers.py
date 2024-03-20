from rest_framework import serializers
from app.models import Users, Roles

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('name',)


class UserCreateSerializer(serializers.ModelSerializer):
    profile_pic = serializers.FileField(required=False)
    # role = RolesSerializer()
    class Meta:
        model = Users
        fields = ('name', 'designation', 'role', 'contact_no', 'pincode', 'password', 'email', 'profile_pic')
        extra_kwargs = {
            'password': {'write_only': True},
            'pincode':{'required':False},
            'profile_pic':{'required':False}
            }
