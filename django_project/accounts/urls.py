# accounts/urls.py
from django.urls import path

from .views import *


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('logout/', custom_logout, name='custom_logout'),
]