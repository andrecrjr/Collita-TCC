import pagarme
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect

from apisite.models import Inventario
pagarme.authentication_key(settings.PAGAR_ME_TOKEN)

def calc_total_boleto(trans):
    valor_total = 0
    for dados in trans:
        valor_total += dados['preco_item']
    valor_total = valor_total * 100
    return str(valor_total)

def request_boleto(request):
    if request.method == 'GET':
        data = Inventario.objects.get(id=request.user.pk)
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
        print(transact)
    return redirect('/marketplace/boletos/')


def paid_boleto(request):
    if request.method == 'GET':
        itens = request.session.get('boleto_' + request.user.username, [])
        print(itens)

