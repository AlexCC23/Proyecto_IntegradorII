from rest_framework import serializers
from .models import Pedido

class PedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Pedido
        fields='__all__'