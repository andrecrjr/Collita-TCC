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


def transaction_filter(request):
    if request.method == "GET":
        transactions = {}
        mes = request.GET.get("mes", "")
        ano = request.GET.get("ano", "")
        qtd = request.GET.get("qtd", "")
        status = request.GET.get("status", "")
        if not qtd:
            qtd = 10
        if not status:
            status = True
        transactions['data'] = list(Transacao.objects.filter(data_boleto_criado__month=mes, 
                                                            data_boleto_criado__year=ano, 
                                                            status_boleto=status)[int(qtd):].values())
        for key, value in enumerate(transactions['data']):
            user = Inventario.objects.get(id=value['usuario_transacao_id'])
            transactions['data'][key]['nome_completo'] = f"{user.usuario.first_name} {user.usuario.last_name}"
        return JsonResponse(transactions, status=200)
