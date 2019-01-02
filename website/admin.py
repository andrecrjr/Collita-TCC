from django.contrib import admin
from apisite.models import *
from transacaosite.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Inventario)
admin.site.register(Item)
admin.site.register(Pedido)