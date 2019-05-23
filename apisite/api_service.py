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
        username = request.GET.get("username", "")
        username_verify = request.GET.get("username_verify", "")
        
        if not qtd:
            qtd = 10
        if status:
            if status == "true":
                status = True
            else:
                status = False
        
        if username_verify:
            user = Inventario.objects.get(usuario__username=username_verify)
            if user:
                return JsonResponse({"username":user.usuario.username}, status=200)
            else:
                return JsonResponse(status=404)
        
        if not username:
            transactions['data'] = list(Transacao.objects.filter(data_boleto_criado__month=mes, 
                                                    data_boleto_criado__year=ano, 
                                                    status_boleto=status).order_by("-id")[:int(qtd)].values())
        elif mes and ano and username:
            usuario = Inventario.objects.get(usuario__username = username)
            transactions['data'] = list(Transacao.objects.filter(data_boleto_criado__month=mes, 
                                                data_boleto_criado__year=ano, 
                                                status_boleto=status, usuario_transacao_id=usuario.id)[:int(qtd)].values())
        for key, value in enumerate(transactions['data']):
            user = Inventario.objects.get(id=value['usuario_transacao_id'])
            transactions['data'][key]['nome_completo'] = f"{user.usuario.first_name} {user.usuario.last_name}"
            transactions['data'][key]['username'] = f"{user.usuario.username}"
        reversed(transactions['data'])
        return JsonResponse(transactions, status=200)
