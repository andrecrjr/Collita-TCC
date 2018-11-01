from django.db import models
from apisite.models import *

# Create your models here.
class Moeda(models.Model):
    nome_moeda = models.CharField(max_length=12, default='Coincoin')

class AtualizaMoeda(models.Model):
    moeda_atual = models.BigIntegerField(default=0)
    moeda_adicionada_removida = models.BigIntegerField(default=0)
    moeda_total = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'atualizacao_do_jogo'

class NotaFiscalMoeda(models.Model):
    inventario_compra = models.ForeignKey(Inventario,  on_delete=models.CASCADE, related_name='ultima_compra')
    valor_comprado = models.IntegerField()
    data_transact =  models.DateTimeField(auto_now=True)
    atualiza_moeda = models.ForeignKey(AtualizaMoeda, on_delete=models.CASCADE, related_name='quantia_moeda')
    
    class Meta:
        db_table = 'nota_fiscal'
        get_latest_by = "order_date"
        