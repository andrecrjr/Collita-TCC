from transacaosite.models import *
from django.http import JsonResponse


def item_usuario(request, pk):
    inventario = {}
    inventario['data'] = list(ItemCompra.objects.filter(id_usuario=pk, quantidade__gt=0).values())
    if inventario['data'] > []:
        for key, value in enumerate(inventario['data']):
            item = Item.objects.get(id_item=value['item_id'])
            inventario['data'][key]['nome_item'] = item.nome_item
    else:
        inventario['data'] = []
    return JsonResponse(inventario, status=200)

