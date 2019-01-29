from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import *


class PedidoList(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        user = self.kwargs['pk']
        return Pedido.objects.filter(usuario_pedido=user)    


class InventarioDetails(generics.RetrieveAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

