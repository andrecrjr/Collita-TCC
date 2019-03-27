from rest_framework import serializers
from .models import Inventario, User
from transacaosite.models import Item, Transacao, ItemInfo
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id_item', 'nome_item')

class ItemInfoSerializer(serializers.ModelSerializer):
    item = ItemSerializer(required=True)
    class Meta:
        model = ItemInfo
        fields = ('id', 'item', 'quantidade')

class ItemUsuarioSerializer(serializers.ModelSerializer):
    item_comprado = ItemInfoSerializer(required=True)

    class Meta:
        model = Transacao
        fields = ('id','item_comprado')

class InventarioSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(required=True)

    class Meta:
        model = Inventario
        fields = ('usuario',)

    def create(self, validated_data):
        user_data = validated_data.pop('usuario')
        perfil = UserSerializer.create(UserSerializer(), validated_data=user_data)
        inventario = Inventario.objects.update_or_create(usuario=perfil)
        return inventario


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')
