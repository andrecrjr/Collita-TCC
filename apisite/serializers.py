from rest_framework import serializers
from .models import Inventario, User
from transacaosite.models import Item, Transacao
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemsUsuarioSerializer(serializers.ModelSerializer):
    item_comprado = ItemSerializer(required=True)

    class Meta:
        model = Transacao
        fields = '__all__'

    def create_inventario(self, validated_data):
        item_data = validated_data.pop('item_comprado')
        items_inventario = ItemSerializer.create(ItemSerializer(), validated_data=item_data)
        inventario = Transacao.objects.update_or_create(usuario=items_inventario)
        return inventario


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
