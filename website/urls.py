from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='Home'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='Login'),
    path('cadastro/', signup, name='Cadastro')
]