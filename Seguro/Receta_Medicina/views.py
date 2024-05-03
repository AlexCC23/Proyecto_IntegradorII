from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Receta_Medicina 
from .serializers import Receta_MedicinaSerializers 


class Receta_MedicinaView(viewsets.ModelViewSet):
    serializer_class=Receta_MedicinaSerializers
    queryset=Receta_Medicina.objects.all() 