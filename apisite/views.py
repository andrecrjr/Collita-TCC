from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from transacaosite.models import *


class InventarioItemList(generics.ListAPIView):
    serializer_class = ItemInfoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user = self.kwargs['pk']
        return ItemCompra.objects.filter(id_usuario=user, quantidade__gt=0)


class InventarioDetails(generics.RetrieveAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

