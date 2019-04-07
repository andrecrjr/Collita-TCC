import pagarme
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect

from apisite.models import Inventario
from transacaosite.models import *

pagarme.authentication_key(settings.PAGAR_ME_TOKEN)

def calc_total_boleto(trans):
    valor_total = 0
    for dados in trans:
        preco_com_quantidade = dados['preco_item'] * dados['quantidade']
        valor_total += preco_com_quantidade
    valor_total = valor_total * 100
    return str(valor_total)

def request_boleto(request):
    if request.method == 'GET':
        usuario = Inventario.objects.get(id=request.user.pk)
        trans = request.session.get('boleto_' + request.user.username)
        valor_total = calc_total_boleto(trans)
        params = {
                'amount': valor_total,
                'payment_method': 'boleto',
                'customer': {
                    'type': 'individual',
                    'country': 'br',
                    'email': 'andre-carlos@live.com',
                    'name': 'andre carlos',
                    'documents': [
                        {
                            'type': 'cpf',
                            'number': '00000000000'
                        }
                    ]
                }
            }
        transact = pagarme.transaction.create(params)
        Transacao.objects.create(usuario_transacao=usuario,
                                                status_boleto=False,
                                                codigo_boleto=transact['tid'])
        print(transact['tid'])
        request.session['codigo_boleto'] = transact['tid']
        return redirect('/marketplace/boleto/')

'''
def paid_boleto(request):
    if request.method == 'GET':
        itens = request.session['boleto_' + request.user.username]
        codigo = request.session['codigo_boleto']
        if itens and codigo:
            #trans = Transacao.objects.get(codigo_boleto=codigo)
            for dados in itens:
                item = Item.objects.get(id_item=int(dados['id_item']))
                pedido = ItemCompra.objects.create(transacao=trans, item=item, quantidade=1, id_usuario=request.user.pk)
                pedido.save()
            #itens.clear()
            #codigo.clear()
            #request.session.modified = True
'''
