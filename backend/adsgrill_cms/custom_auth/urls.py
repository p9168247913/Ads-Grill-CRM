from django.urls import path
from custom_auth import login

urlpatterns = [
    path("login/", login.authLogin.as_view()),
    path("logout/", login.LogoutView.as_view())
]