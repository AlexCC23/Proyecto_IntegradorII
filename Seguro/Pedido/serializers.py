from rest_framework import serializers
from .models import Pedido

class PedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Pedido
        fields='__all__'


class EmailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    dni = serializers.CharField(max_length=8)
    email = serializers.EmailField()
    pdf1 = serializers.FileField()
    pdf2 = serializers.FileField()
    
class SMSSerializer(serializers.Serializer):
    to = serializers.CharField(max_length=15)
    text = serializers.CharField(max_length=160)