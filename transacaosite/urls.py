from django.urls import path
from .views import *

urlpatterns = [
    path('marketplace/cart/', cart_marketplace, name='checkout'),
    path('json/pagseguro_session/', session_id),
]
