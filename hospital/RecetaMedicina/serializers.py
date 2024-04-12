from rest_framework import serializers
from .models import RecetaMedicina

class RecetaMedicinaSerializers(serializers.ModelSerializer):
    class Meta:
        model=RecetaMedicina
        fields='__all__'