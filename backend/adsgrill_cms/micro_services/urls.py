from django.urls import path
from micro_services.users_management import users

urlpatterns = [
    path("users/", users.UsersView.as_view()),
]