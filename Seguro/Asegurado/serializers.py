from rest_framework import serializers
from .models import Asegurado

class AseguradoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Asegurado
        fields='__all__'