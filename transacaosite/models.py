from django.db import models
from apisite.models import Inventario

class Item(models.Model):
    nome_item = models.CharField(max_length=35)
    valor_item = models.IntegerField()

    class Meta:
        db_table = 'item'
        verbose_name = 'item do jogo'
        verbose_name_plural = 'itens'

    def __str__(self):
        return "%s" % self.nome_item

class Pedido(models.Model):

    item_pedido = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_pedido")
    usuario_pedido = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name="inventario_pedido")
    codigo_pagseguro = models.CharField(unique=True, blank=True, max_length=60)

    def __str__(self):
        if self.codigo_pagseguro:
            return "Usuário: %s, Codigo pagseguro: %s" % (self.usuario_pedido, self.codigo_pagseguro)
        else:
            return "%s ainda não pagou" % self.usuario_pedido.usuario
