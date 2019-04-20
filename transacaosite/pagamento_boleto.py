import pagarme
from django.conf import settings
from django.shortcuts import redirect
from transacaosite.models import *
from apisite.models import Inventario
import requests


pagarme.authentication_key(settings.PAGAR_ME_TOKEN)

def calc_total_boleto(trans):
    valor_total = 0
    for dados in trans:
        preco_com_quantidade = float(dados['preco_item']) * int(dados['quantidade'])
        valor_total += preco_com_quantidade
    valor_total = valor_total * 100
    valor_total = int(valor_total)
    return str(valor_total)

def params_boleto(valor_total, email_usuario, nome_usuario):
    params = {
        'amount': valor_total,
        'payment_method': 'boleto',
        'customer': {
            'type': 'individual',
            'country': 'br',
            'email': email_usuario,
            'name': nome_usuario,
            'documents': [
                {
                    'type': 'cpf',
                    'number': '00000000000'
                }
            ]
        }
    }
    return params

def request_boleto(request):
    if request.method == 'GET':
        usuario = Inventario.objects.get(id=request.user.pk)
        trans = request.session.get('boleto_' + request.user.username)
        valor_total = calc_total_boleto(trans)
        params = params_boleto(valor_total, request.user.email, request.user.first_name)
        transact = pagarme.transaction.create(params)
        Transacao.objects.create(usuario_transacao=usuario,
                                                status_boleto=False,
                                                codigo_boleto=transact['tid'])
        request.session['codigo_boleto'] = transact['tid']
        return redirect('/marketplace/boleto/')


def paid_boleto(request):
    if request.method == 'GET':
        itens = request.session['boleto_' + request.user.username]
        codigo = request.session['codigo_boleto']
        if itens and codigo:
            trans = Transacao.objects.get(codigo_boleto=codigo)
            for dados in itens:
                item = Item.objects.get(id_item=int(dados['id_item']))
                pedido = ItemCompra.objects.create(item=item,
                                                   item_transacao=trans,
                                                   quantidade=dados['quantidade'],
                                                   id_usuario=request.user.pk)
                pedido.save()
            trans.status_boleto = True
            trans.save()
            itens.clear()
            del codigo
            request.session.modified = True
        return redirect('/marketplace/')
