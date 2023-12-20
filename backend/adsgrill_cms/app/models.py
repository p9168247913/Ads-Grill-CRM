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
    contact_no = models.CharField(max_length=15, null=True, blank=False )
    profile_pic = models.FileField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    groups = models.ManyToManyField('auth.Group', related_name='users_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='users_set', blank=True)
    pincode = models.CharField(max_length=15, null=True, blank=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
class Access_requests(models.Model):
    admin = models.ForeignKey(Users, on_delete=models.CASCADE,null=False, blank=False, related_name='admin_access_requests')
    super_admin = models.ForeignKey(Users,on_delete=models.CASCADE,null=False, blank=False, related_name='super_admin_access_requests')
    feature_requested = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)


class Source(models.Model):
    name = models.CharField(null=False, blank=True, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(null=False, blank=True, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name
    
class LeadStatus(models.Model):
    name = models.CharField(null=False,blank=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name
    
class Lead(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,null=False, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE,null=False, blank=True, related_name='leadSource')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,null=False, blank=True, related_name='leadTag')
    status = models.ForeignKey(LeadStatus, on_delete=models.CASCADE, null=False, blank=True, related_name="LeadStatus")
    client_name = models.CharField(null=False, blank=True, max_length=20)
    contact_no = models.CharField(null=False, blank=True, max_length=15)
    email = models.EmailField(null=False, max_length=30)
    country = models.CharField(null=False, blank=True, max_length=30)
    state = models.CharField(null=False, blank=True, max_length=30)
    city = models.CharField(null=False, blank=True, max_length=30)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
    
    def __str__(self):
        return self.client_name
    




