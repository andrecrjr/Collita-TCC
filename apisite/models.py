from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



#após salvar no banco do perfil crie um inventário de sua instancia
@receiver(post_save, sender=User)
def create_inventario_user(sender, instance, created, **kwargs):
    if created:
        print(instance)
        Inventario.objects.create(usuario=instance)

class Inventario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inventario_usuario')

    class Meta:
        db_table = 'inventario'

    def __str__(self):
        return "%s" % (self.usuario)
    
    def get_absolute_url(self):
        return "/perfil/%s" % (self.id)