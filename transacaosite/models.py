from django.db import models
from apisite.models import Inventario


class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    nome_item = models.CharField(max_length=35)
    valor_item = models.DecimalField(decimal_places=2, max_digits=5)
    imagem_item = models.FileField(verbose_name='Imagem do item', upload_to='item_folder/', default='')

    class Meta:
        db_table = 'item'
        verbose_name = 'item do jogo'
        verbose_name_plural = 'itens'

    def __str__(self):
        return "%s" % self.nome_item


class Transacao(models.Model):

    class Meta:
        db_table = 'transacao'
        verbose_name = 'transação do site'
        verbose_name_plural = 'transações do site'

    usuario_transacao = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name="transacao_inventario")
    status_boleto = models.BooleanField(verbose_name='Status do boleto', default=False)
    codigo_boleto = models.CharField(max_length=47, default=0)

    def __str__(self):
        if self.status_boleto is not False:
            return "Boleto pago, transação aceita"
        else:
            return "%s ainda não pagou" % self.usuario_transacao


class ItemCompra(models.Model):

    class Meta:
        db_table = 'item_transacao'
        verbose_name = 'item da compra'
        verbose_name_plural = 'items da compra'

    item_transacao = models.ForeignKey(Transacao, related_name="item_transacao", on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_itens')
    quantidade = models.IntegerField(default=0)
    id_usuario = models.BigIntegerField()

    def __str__(self):
        return "Item: %s \n Quantidade: %d" % (self.item, self.quantidade)
