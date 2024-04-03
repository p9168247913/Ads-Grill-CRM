from django.contrib import admin
from app.models import Users, Access_requests, Roles

# Register your models here.
admin.site.register(Users)
admin.site.register(Access_requests)
admin.site.register(Roles)

