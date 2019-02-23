from django.urls import path
from .views import *

urlpatterns = [
    path('json/pagseguro_session/', session_id),
]
