from rest_framework import serializers
from .models import Guia

class GuiaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Guia
        fields='__all__'