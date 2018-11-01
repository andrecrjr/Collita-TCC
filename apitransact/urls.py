from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('notafiscal/', NotaFiscalView.as_view(), name='Nota Fiscal api'),
    
]