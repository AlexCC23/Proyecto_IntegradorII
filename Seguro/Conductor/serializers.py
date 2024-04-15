from rest_framework import serializers
from .models import Conductor

class ConductorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Conductor
        fields='__all__'