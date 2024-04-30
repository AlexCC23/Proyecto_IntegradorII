from rest_framework import serializers
from .models import Medicina

class MedicinaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Medicina
        fields='__all__'