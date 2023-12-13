from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.utils import timezone
from django.db import models

# Create your models here.

class Roles(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

class Users(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=25, null=True, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=True, blank=False)
    contact_no = models.CharField(max_length=10, null=True, blank=False )
    profile_pic = models.FileField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    groups = models.ManyToManyField('auth.Group', related_name='users_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='users_set', blank=True)
    pincode = models.CharField(max_length=6, null=True, blank=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
class Access_requests(models.Model):
    admin = models.ForeignKey(Users, on_delete=models.CASCADE,null=False, blank=False, related_name='admin_access_requests')
    super_admin = models.ForeignKey(Users,on_delete=models.CASCADE,null=False, blank=False, related_name='super_admin_access_requests')
    feature_requested = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=20, default='Pending')




