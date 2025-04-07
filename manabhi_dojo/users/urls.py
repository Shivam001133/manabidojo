from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from manabhi_dojo.users.views import (
    home_view,
    dashboard,
    profile_view,
)

app_name = "users"


urlpatterns = [
    path("", home_view, name="home"),
    path("profile/", profile_view, name="profile"),
    path("dashboard/", dashboard, name="dashboard"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
