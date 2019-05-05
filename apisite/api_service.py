from transacaosite.models import *
from django.http import JsonResponse


def item_usuario(request, pk):
    try:
        inventario_game = {}
        user = Inventario.objects.get(id=pk)
        inventario_game['data'] = list(InventarioItemGame.objects.filter(usuario=user, quantidade__gt=0).values())
        print(inventario_game['data'])
        if inventario_game['data'] > []:
            for key, value in enumerate(inventario_game['data']):
                item = Item.objects.get(id_item=value['item_id'])
                inventario_game['data'][key]['nome_item'] = item.nome_item
            return JsonResponse(inventario_game, status=200)
        else:
            inventario_game['data'] = []
        return JsonResponse(inventario_game, status=200)
    except:
        return JsonResponse({'status':'error', 'message':'não existe usuario'}, status=404)

