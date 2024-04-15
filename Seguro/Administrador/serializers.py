from rest_framework import serializers
from .models import Administrador

class AdministradorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Administrador
        fields='__all__'