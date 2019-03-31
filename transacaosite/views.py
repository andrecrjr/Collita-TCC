import json
from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.csrf import csrf_exempt
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
def generate_boleto(request):
    #gerar boleto com o valor dos itens
    if request.method == 'GET':
        boletao = 'boleto_' + request.user.username
        if request.session.get(boletao):
            data_cart = request.session.get(request.user.username)
            if len(data_cart) > 0:
                request.session[boletao] = data_cart
                request.session[request.user.username] = []
                request_boleto(request)
                #Transacao.objects.create(usuario_transacao=usuario, status_boleto=False, codigo_boleto=url_boleto)
                return redirect('/marketplace/boleto/')
            else:
                return render(request, 'marketplace.html', {'error': 'Você não tem itens no carrinho'})

    return redirect('/marketplace/')


def delete_cart(request):
    if request.method == 'GET':
        data = request.session.get(request.user.username)
        if data:
            data.clear()
            request.session.modified = True
            return HttpResponse('apagado com sucesso')
        else:
            return HttpResponse('nada')