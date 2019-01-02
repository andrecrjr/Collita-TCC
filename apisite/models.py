from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


#após criar o usuário, crie o seu perfil no banco
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):

    class Meta:
        db_table = 'perfil'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_usuario', unique=True)

    def __str__(self):
        return "%s" % self.user

#após salvar no banco do perfil crie um inventário de sua instancia
@receiver(post_save, sender=Profile)
def create_inventario_user(sender, instance, created, **kwargs):
    if created:
        Inventario.objects.create(usuario=instance)

class Inventario(models.Model):
    usuario = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='inventario_usuario')

    class Meta:
        db_table = 'inventario'

    def __str__(self):
        return "%s" % (self.usuario)