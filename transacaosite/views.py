import json
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .pagamento_boleto import request_boleto
from .models import Transacao


@csrf_exempt
def add_item_cart(request):
    if request.method == 'POST':
        usuario = request.user.username
        cart_session = request.session.get(usuario, [])
        data = json.loads(request.body)
        cart_session.append(data)
        for id, datas in enumerate(cart_session):
            cart_session[id]['id_compra'] = id
        request.session[usuario] = cart_session
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def list_items(request):
    items = request.session.get(request.user.username)
    return HttpResponse(json.dumps(items), content_type="application/json")


@csrf_exempt
def update_cart_same_item(request, id, new_quantity):
    if request.method == 'PUT':
        cart = request.session[request.user.username]
        cart[id]['quantidade'] = int(cart[id]['quantidade'])
        cart[id]['quantidade'] += new_quantity
        cart[id]['quantidade'] = str(cart[id]['quantidade'])
        request.session.modified = True
        return HttpResponse(status=200)


@csrf_exempt
def delete_item(request, id):
    if request.method == 'PUT':
        cart = request.session.get(request.user.username)
        del cart[id]
        for id, datas in enumerate(cart):
            cart[id]['id_compra'] = id
        request.session.modified = True
        return HttpResponse(status=200)


def generate_boleto(request):
    if request.method == 'GET':
        boleto = 'boleto_' + request.user.username
        boleto_nao_pago = Transacao.objects.filter(status_boleto=False, usuario_transacao_id=request.user.pk)
        if not boleto_nao_pago:
            data_cart = request.session.get(request.user.username)
            if data_cart and len(data_cart) > 0:
                request.session[boleto] = data_cart
                request.session[request.user.username] = []
                return request_boleto(request)
            else:
                return render(request, 'marketplace.html', {'error': 'Você não tem itens no carrinho'})
        else:
            return render(request, 'marketplace.html', {'error': 'Você ainda tem boleto esperando pagamento'})

    return redirect('/marketplace/')


def delete_cart(request):
    if request.method == 'GET':
        data = request.session.get(request.user.username)
        if data:
            data.clear()
            request.session.modified = True
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=200)