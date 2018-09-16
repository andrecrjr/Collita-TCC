from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    profile_id = serializers.CharField(source='user.id')
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    moeda = serializers.CharField(source='inventario_usuario.moeda')
    class Meta:
        model = Profile
        fields = ('profile_id','username', 'first_name','last_name', 'moeda', )