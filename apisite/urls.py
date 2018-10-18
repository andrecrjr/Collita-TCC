from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('perfil/', ProfileList.as_view(), name='Profile api'),
    path('perfil/<int:pk>/', ProfileDetails.as_view()),
    path('item/', ItemList.as_view(), name='Items api'),
    path('item/<int:pk>/', ItemDetails.as_view(), name='Items api'),
    path('inventario/',InventarioList.as_view(), name='Inventario usuários'),
    path('inventario/<int:pk>/',InventarioDetails.as_view(), name='Inventario do usuário'),
    path('auth/', include('rest_auth.urls')),
]