from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from manabhi_dojo.users.views import (
    home_view,
    user_detail_view,
    user_redirect_view,
    user_update_view,
    signup
)

app_name = "users"
urlpatterns = [
    path("home/", home_view),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
    path('signup/', view=signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]