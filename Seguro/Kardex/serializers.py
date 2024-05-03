from rest_framework import serializers
from .models import Kardex

class KardexSerializers(serializers.ModelSerializer):
    class Meta:
        model=Kardex
        fields='__all__'