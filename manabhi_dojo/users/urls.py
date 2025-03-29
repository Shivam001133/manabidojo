"""
URL configuration for users.
"""
from django.urls import path
from manabhi_dojo.users.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
