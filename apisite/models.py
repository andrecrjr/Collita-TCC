from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Item(models.Model):
    nome_item = models.CharField(max_length=35)
    valor_item = models.IntegerField()

    class Meta:
        db_table = 'item'
        verbose_name = 'item do jogo'
        verbose_name_plural = 'itens'

    def __str__(self):
        return "%s" % self.nome_item

#após criar o usuário, crie o seu perfil no banco
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_usuario', unique=True)

    def __str__(self):
        return "%s" % self.user

#após salvar no banco do perfil crie um inventário de sua instancia
@receiver(post_save, sender=Profile)
def create_inventario_user(sender, instance, created, **kwargs):
    if created:
        Inventario.objects.create(usuario=instance)

class Inventario(models.Model):
    usuario = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='dono_inventario')
    moeda = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.usuario, self.moeda)

class Transaction(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='pega_item')
    inventario = models.OneToOneField(Inventario, on_delete=models.CASCADE)
    data_transact = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s, %s" % (self.item, self.inventario, self.data_transact)