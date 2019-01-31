from pagseguro.api import PagSeguroItem, PagSeguroApi
from django.conf import settings

#from pagseguro.models import Transaction, Checkout, TransactionHistory

def checkout_app(item):
    pagseguro = PagSeguroApi(email=settings.PAGSEGURO_EMAIL,token=settings.PAGSEGURO_TOKEN)
    pagseguro.add_item(item)
    data = pagseguro.checkout()
    if data['status_code'] == 200:
        return data
    else:
        return False


def add_trasaction_item(id, nome, valor_item):
        new_item = PagSeguroItem(id=id, description=nome, amount=valor_item, quantity=1)
        data = checkout_app(new_item)
        return data





