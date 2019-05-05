from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from transacaosite.models import *

class InventarioUpdate(generics.UpdateAPIView):
    serializer_class = ItemInfoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def update(self, request, *args, **kwargs):
        item = self.kwargs['item']
        user = self.kwargs['pk']
        try:
            user = Inventario.objects.get(id=user)
            item = Item.objects.get(id_item=item)
        except:
            return JsonResponse({'error' : 'não existe usuario ou item'}, status=404)

        if self.request.query_params.get('quantidade'):
            qtd = self.request.query_params.get('quantidade')
        else:
            return JsonResponse({'error' : 'Nenhuma quantidade atribuida'}, status=422)
        if 0 > int(qtd):
            return JsonResponse({'status' : 'error', 'Message': 'Quantidade menor que zero'}, status=400)
        else:
            serializer = InventarioItemGame.objects.get(usuario=user, item=item)
            serializer.quantidade = qtd
            serializer.save()
            return JsonResponse({'message':'Quantidade atualizada com sucesso'}, status=200)


class InventarioDetails(generics.RetrieveAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

