from rest_framework import serializers
from .models import *



class AtualizaMoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtualizaMoeda
        fields=('__all__')


class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscalMoeda
        fields = ('id','atualiza_moeda',)

    def create(self, validated_data):
        dados = validated_data.pop('atualiza_moeda')
        movimentacao = AtualizaMoedaSerializer.create(AtualizaMoedaSerializer(), validated_data=dados)
        movimentacao_compra_moeda = NotaFiscalMoeda.objects.update_or_create(atualiza_moeda=movimentacao)
        return movimentacao_compra_moeda
