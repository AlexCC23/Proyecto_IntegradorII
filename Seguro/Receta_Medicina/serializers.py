from rest_framework import serializers
from .models import Receta_Medicina

class Receta_MedicinaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Receta_Medicina
        fields='__all__'