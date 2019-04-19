from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('inventario/<int:pk>/', InventarioDetails.as_view(), name='Inventario do usuário'),
    path('inventario/items/<int:pk>/', InventarioItemList.as_view(), name="Items do usuário"),
    path('inventario/<int:pk>/<int:transacao>/', InventarioUpdate.as_view(), name="Atualizar inventario")
]