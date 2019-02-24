from django.urls import path
from .views import *

'''
json do cart
capturar o json do javascript e fazer get no front
'''
urlpatterns = [
    path('add_item/', add_item_cart, name='add_item'),
    path('delete/', delete_cart, name='delete')
]
