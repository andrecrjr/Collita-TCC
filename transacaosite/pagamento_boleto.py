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
        valor_total += dados['preco_item']
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
        #Transacao.objects.create(usuario_transacao=usuario,
        #                                           status_boleto=False,
        #                                              codigo_boleto=transact['tid'])
        print(transact['tid'])
        request.session['codigo_boleto'] = transact['tid']
        return redirect('/marketplace/boleto/')

'''
def paid_boleto(request):
    if request.method == 'GET':
        itens = request.session['boleto_' + request.user.username]
        #trans = Transacao.objects.get(codigo_boleto=codigo)
        if itens:
            for data in itens:
                print(data)
                itens = ItemCompra(data)
                #trans.item_comprado = item
        #trans.clear()
        #request.session.modified = True
'''
