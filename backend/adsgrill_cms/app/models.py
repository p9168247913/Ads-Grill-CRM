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
    role = models.ForeignKey(Roles, on_delete=models.PROTECT)
    designation = models.CharField(max_length=20, null=True, blank=False)
    contact_no = models.CharField(max_length=15, null=True, blank=False )
    profile_pic = models.FileField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    groups = models.ManyToManyField('auth.Group', related_name='users_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='users_set', blank=True)
    pincode = models.CharField(max_length=15, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

class Client(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=25, null=True, blank=False)
    email = models.EmailField(null=False, blank=False)
    pincode = models.CharField(max_length=15, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email
    
class Access_requests(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.PROTECT, null=False, blank=False, related_name='sender')
    receiver = models.ForeignKey(Users, on_delete=models.PROTECT, null=False, blank=False, related_name='receiver')
    feature_requested = models.CharField(null=False, blank=False)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.feature_requested


class Source(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name
    
class LeadStatus(models.Model):
    name = models.CharField(unique=True, null=False,blank=False, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name
    
class Lead(models.Model):
    sales_man = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False)
    source = models.ForeignKey(Source,on_delete=models.PROTECT, null=True, blank=False, related_name='leadSource')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, null=True, blank=False, related_name='leadTag')
    client_name = models.CharField(null=True, blank=False, max_length=20)
    contact_no = models.CharField(null=True, blank=False, max_length=15)
    email = models.EmailField(null=True, max_length=30)
    country = models.CharField(null=True, blank=False, max_length=30)
    state = models.CharField(null=True, blank=False, max_length=30)
    city = models.CharField(null=True, blank=False, max_length=30)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
    
    def __str__(self):
        return self.client_name

class Sale(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.PROTECT, null=True, blank=False)
    assignee = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False)
    status = models.ForeignKey(LeadStatus, on_delete=models.PROTECT, null=True, blank=False, related_name="LeadStatus")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.lead.client_name
    
class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, db_index=True)
    name = models.CharField(max_length=65, null=False, blank=False)
    key = models.CharField(max_length=10, null=True, blank=False)
    type = models.CharField(max_length=25, null=False, blank=False)
    status = models.CharField(max_length=15, null=False, blank=False)
    lead = models.ForeignKey(Users, on_delete=models.PROTECT, null=False, blank=False, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name
    
class Sprint(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, db_index=True, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    duration = models.DurationField(null=True, blank=False, default=timezone.timedelta(days=7))
    status = models.CharField(max_length=15, null=False, blank=False)
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=False)
    goal = models.CharField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.PROTECT, db_index=True)
    name = models.CharField(max_length=25, null=False, blank=True)
    description = models.CharField(null=False, blank=False)
    status = models.CharField(max_length=15, null=False, blank=False)
    est_duration = models.DurationField(null=True, blank=False)
    act_duration = models.DurationField(null=True, blank=False)
    rep_man = models.ForeignKey(Users, on_delete=models.PROTECT, null=False, blank=False, related_name='task_rep_man')
    assignee = models.ForeignKey(Users, on_delete=models.PROTECT, null=False, blank=False, related_name='task_assignee')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name

class SubTask(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.PROTECT, db_index=True)
    task = models.ForeignKey(Task, on_delete=models.PROTECT, db_index=True)
    name = models.CharField(max_length=25, null=False, blank=True)
    description = models.CharField(null=False, blank=False)
    status = models.CharField(max_length=15, null=False, blank=False)
    est_duration = models.DurationField(null=True, blank=False)
    act_duration = models.DurationField(null=True, blank=False)
    rep_man = models.ForeignKey(Users, on_delete=models.PROTECT, null=False, blank=False, related_name='subtask_rep_man')
    assignee = models.ForeignKey(Users, on_delete=models.PROTECT, null=False, blank=False, related_name='subtask_assignee')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name











    




