from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from manabhi_dojo.users.views import (
    home_view,
    user_detail_view,
    user_redirect_view,
    user_update_view,
    sign_up,
    dashboard,
    profile_view,
)

app_name = "users"


urlpatterns = [
    path("", home_view, name="home"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("profile/", profile_view, name="profile"),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/', sign_up, name='signup'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
