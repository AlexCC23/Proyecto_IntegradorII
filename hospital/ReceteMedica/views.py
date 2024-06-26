from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Receta #modelo para crear la BD
from .serializers import RecetaSerializers #modelo del API, los campos que ve a traer la API de la BD 

# Create your views here.

#trae todos los datos del modelo Receta,
class RecetaView(viewsets.ModelViewSet):
    serializer_class=RecetaSerializers
    queryset=Receta.objects.all() #este sentencia es oara trear todos los datos de los campos indicados en serializers
     #este es como el json