from rest_framework import serializers
from .models import Puntuacion

class PuntuacionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Puntuacion
        fields='__all__'

