from rest_framework import serializers
from .models import *
from transacaosite.models import *
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('user',)
    
    def create_user(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of profile
        :return: returns a successfully created profile record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile = Profile.objects.update_or_create(user=user)
        return profile


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    item_pedido = ItemSerializer(required=True)
    class Meta:
        model = Pedido
        fields = ('id', 'item_pedido')
    
    def create_inventario(self, validated_data):
        item_data = validated_data.pop('item_pedido')
        items_inventario = ItemSerializer.create(ItemSerializer(), validated_data=item_data)
        inventario = Pedido.objects.update_or_create(usuario=items_inventario)
        return inventario

class InventarioSerializer(serializers.ModelSerializer):
    usuario = ProfileSerializer(required=True)
    class Meta:
        model = Inventario
        fields = ('usuario',)

    def create(self, validated_data):
        user_data = validated_data.pop('usuario')
        perfil = ProfileSerializer.create(ProfileSerializer(), validated_data=user_data)
        inventario = Inventario.objects.update_or_create(usuario=perfil)
        return inventario


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')