from django.contrib import admin
from apisite.models import *
from apitransact.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Inventario)
admin.site.register(Item)
admin.site.register(Moeda)
admin.site.register(NotaFiscalMoeda)
admin.site.register(AtualizaMoeda)
