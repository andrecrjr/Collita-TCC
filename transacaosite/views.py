import json
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from .pagamento_boleto import request_boleto


@csrf_exempt
def add_item_cart(request):
    if request.method == 'POST':
        usuario = request.user.username
        cart_session = request.session.get(usuario, [])
        data = json.loads(request.body)
        cart_session.append(data)
        request.session[usuario] = cart_session
        return HttpResponse(status=200)
    else:
        return HttpResponse('erro 400', status=400)


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
        if not request.session.get(boletao):
            data_cart = request.session.get(request.user.username)
            if len(data_cart) > 0:
                request.session[boletao] = data_cart
                request.session[request.user.username] = []
                return request_boleto(request)
            else:
                return render(request, 'marketplace.html', {'error': 'Você não tem itens no carrinho'})
        else:
            return render(request, 'marketplace.html', {'error': 'Você ainda tem boleto em esperando pagamento'})

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