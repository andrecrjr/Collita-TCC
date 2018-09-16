from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileList.as_view(), name='Profile api'),
    path('<int:pk>/', ProfileDetails.as_view())
]