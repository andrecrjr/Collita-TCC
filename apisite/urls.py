from django.urls import path, include
from .views import *
from .api_service import *

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('inventario/<int:pk>/', InventarioDetails.as_view(), name='Inventario do usuário'),
    path('inventario/items/<int:pk>/', item_usuario, name="Items do usuário"),
    path('inventario/<int:pk>/<int:item>/', InventarioUpdate.as_view(), name="Atualizar inventario")
]