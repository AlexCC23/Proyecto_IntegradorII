from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Administrador 
from .serializers import AdministradorSerializers 


class AdministradorView(viewsets.ModelViewSet):
    serializer_class=AdministradorSerializers
    queryset=Administrador.objects.all() 
