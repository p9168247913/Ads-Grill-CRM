from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField
import os
# Create your models here.
class Roles(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    def __str__(self):
        return self.name
class Users(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=40, null=True, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    role = models.ForeignKey(Roles, on_delete=models.PROTECT)
    designation = models.CharField(max_length=30, null=True, blank=False)
    contact_no = models.CharField(max_length=15, null=True, blank=False )
    profile_pic = models.FileField(upload_to='uploads/users/profile/', null=True, blank=True)
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
    role = models.ForeignKey(Roles, on_delete=models.PROTECT)
    name = models.CharField(max_length=25, null=True, blank=False)
    email = models.EmailField(null=False, blank=False)
    pincode = models.CharField(max_length=15, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField('auth.Group', related_name='client_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='client_set', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    def __str__(self):
        return self.email
class Access_requests(models.Model):
    sender = models.IntegerField(null=False, blank=False)
    receiver = models.IntegerField(null=False, blank=False)
    feature_requested = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
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
    name = models.CharField(unique=True, null=False,blank=False, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    def __str__(self):
        return self.name
class Lead(models.Model):
    sales_man = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False)
    source = models.ForeignKey(Source,on_delete=models.PROTECT, null=True, blank=False, related_name='leadSource')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, null=True, blank=False, related_name='leadTag')
    client_name = models.CharField(null=True, blank=False, max_length=40)
    contact_no = models.CharField(null=True, blank=False, max_length=15)
    email = models.EmailField(null=True, max_length=40)
    country = models.CharField(null=True, blank=False, max_length=30)
    state = models.CharField(null=True, blank=False, max_length=30)
    city = models.CharField(null=True, blank=False, max_length=30)
    requirement=models.CharField(null=True,blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
    is_assigned = models.BooleanField(null=False, blank=False, default=False)
    def __str__(self):
        return self.client_name
class Sale(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.PROTECT, null=True, blank=False)
    assignee = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False)
    status = models.ForeignKey(LeadStatus, on_delete=models.PROTECT, null=True, blank=False, related_name="LeadStatus")
    remark=models.CharField(null=True,blank=True)
    sale_status=models.CharField(null=True,blank=False,max_length=30)
    temp_data=models.TextField(null=True,blank=True)
    quot_data = models.TextField(null=True, blank=True)
    follow_date = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(null=False, blank=False, default=False)
    def __str__(self):
        return self.lead.client_name
def default_attachments():
    return []
class Project(models.Model):
    reporter = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False, db_index=True, related_name='pro_reporter')
    team_lead = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False, db_index=True, related_name='pro_team_lead')
    client = models.ForeignKey(Users, null=True, blank=False, on_delete=models.PROTECT, db_index=True, related_name='pro_client')
    name = models.CharField(null=False, blank=False)
    key = models.CharField(null=True, blank=False)
    type = models.CharField(null=False, blank=False)
    status = models.CharField(max_length=30, null=False, blank=False, default='to_do')
    attachments = ArrayField(models.FileField(), blank=True, default=default_attachments)
    host_address = models.CharField(null=True, blank=False)
    tech_stacks = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    def __str__(self):
        return self.name
class Sprint(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, db_index=True, null=False, blank=False)
    reporter = models.ForeignKey(Users, on_delete=models.PROTECT, db_index=True, null=True, blank=False)
    key = models.CharField(null=True, blank=False)
    name = models.CharField(null=False, blank=False)
    description = models.TextField(null=True, blank=False)
    status = models.CharField(max_length=30, null=False, blank=False, default='to_do')
    exp_duration = models.DurationField(null=False, blank=False, default=timezone.timedelta(days=7))
    org_duration = models.DurationField(null=True, blank=False)
    start_date = models.DateTimeField(null=True, blank=False)
    end_date = models.DateTimeField(null=True, blank=False)
    goal = models.CharField(null=True, blank=False)
    is_started = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    def __str__(self):
        return self.name
class Issue(models.Model):
    parent_issue = models.ManyToManyField('self', symmetrical=False,db_index=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, db_index=True, null=False, blank=False)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, db_index=True, null=False, blank=False)
    reporter = models.ForeignKey(Users, on_delete=models.PROTECT, null=False, blank=False, related_name='task_rep_man')
    team_lead = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False, db_index=True, related_name='issue_team_lead')
    title = models.CharField(null=False, blank=True)
    key=models.CharField(null=True, blank=True)
    description = models.TextField(null=True, blank=False)
    type= models.CharField(max_length=30, null=False, blank=False)
    priority = models.CharField(max_length=30, null=True, blank=False)
    status = models.CharField(max_length=30, null=False, blank=False, default='to_do')
    attachments = ArrayField(models.FileField(), blank=True, default=default_attachments)
    exp_duration = models.DurationField(null=True, blank=False)
    org_duration = models.DurationField(null=True, blank=False)
    assignee = models.ForeignKey(Users, db_index=True, on_delete=models.CASCADE, related_name='task_assignee')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    def __str__(self):
        return self.title
class LinkedIssue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False, db_index=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=False, blank=False, db_index=True)
    source = models.ForeignKey(Issue, db_index=True, on_delete=models.CASCADE, related_name='source_issues')
    destination = models.ForeignKey(Issue, on_delete=models.CASCADE, db_index=True, related_name='destination_issue')
    type = models.CharField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
class WorkLog(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=False, blank=False, db_index=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True, blank=False, db_index=True)
    author = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False, db_index = True)
    logged_time = models.DurationField(null=True, blank=False)
    extra_efforts = models.DurationField(null=True, blank=False)
    remaining_time = models.DurationField(null=False,blank=False)
    description = models.TextField(null=True, blank=False)
    attachment = ArrayField(models.FileField(), blank=True, default=default_attachments)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
class Comment(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=True, blank=False, db_index=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True, blank=False, db_index=True)
    author = models.ForeignKey(Users, on_delete=models.PROTECT, null=True, blank=False, db_index = True)
    description = models.TextField(null=True, blank=False)
    attachment = ArrayField(models.FileField(), blank=True, default=default_attachments)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)