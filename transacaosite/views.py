import json
from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from apisite.models import Inventario
from .pagamento_boleto import *
from .models import *


@csrf_exempt
def add_item_cart(request):
    if request.method == 'POST':
        usuario = request.user.username
        cart_session = request.session.get(usuario, [])
        data = json.loads(request.body)
        cart_session.append(data)
        request.session[usuario] = cart_session
        return HttpResponse('ok')
    else:
        return HttpResponse('erro 404')


def list_items(request):
	items = request.session.get(request.user.username)	
	return HttpResponse(json.dumps(items), content_type="application/json")

'''
def delete_item(request, cart_id):
	cart = request.session.get(request.user.username)
	del cart[item_id]
	request.session.modified = True
	return HttpResponse()

@csrf_exempt
def get_total(request):
	total = json.loads(request.body)
	return HttpResponse(json.dumps(total), content_type="application/json")
'''
def cart_to_profile(request):
    #gerar boleto com o valor dos itens
    usuario = Inventario.objects.get(id=request.user.pk)
    nova_transacao = Transacao.objects.create(usuario_transacao=usuario, status_boleto=False)
    data_cart = request.session.get(request.user.username)
    boletao = 'boleto_' + request.user.username
    valor_total = 0
    request.session[boletao] = data_cart
    for dados in data_cart:
        valor_total += dados['preco_item']
    if valor_total > 0:
        request.session[request.user.username] = []
    else:
        pass
    return redirect('/marketplace/boleto/')


def delete_cart(request):
	if request.method == 'GET':
		data = request.session.get(request.user.username)
		if data:
			data.clear()
			request.session.modified = True
			return HttpResponse('apagado com sucesso')
		else:
			return HttpResponse('nada')