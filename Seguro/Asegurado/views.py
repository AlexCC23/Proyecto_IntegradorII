from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Asegurado 
from .serializers import AseguradoSerializers 


class AseguradoView(viewsets.ModelViewSet):
    serializer_class=AseguradoSerializers
    queryset=Asegurado.objects.all() 
