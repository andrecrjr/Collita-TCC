from django.urls import path
from .views import *
#from .pagamento_boleto import paid_boleto

'''
json do cart
capturar o json do javascript e fazer get no front
'''
urlpatterns = [
    path('add_item/', add_item_cart, name='add_item'),
    path('list_item/', list_items, name='list_items'),
    path('delete/', delete_cart, name='delete'),
    path('finalizar/', generate_boleto, name='finalizar'),
    path('create_boleto/', request_boleto, name='request_boleto')
]
