from django.urls import path
from micro_services.users_management import users, roles

urlpatterns = [
    path("users/", users.UsersView.as_view()),
    path("roles/", roles.RolesView.as_view()),
]