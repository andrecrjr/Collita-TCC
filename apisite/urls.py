from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileList.as_view(), name='Profile api'),
    path('<int:pk>/', ProfileDetails.as_view()),
    path('item/', ItemList.as_view(), name='Items api'),
    path('item/<int:pk>/', ItemDetails.as_view(), name='Items api')
]