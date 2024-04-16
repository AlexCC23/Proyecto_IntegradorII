from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Conductor 
from .serializers import ConductorSerializers 


class ConductorView(viewsets.ModelViewSet):
    serializer_class=ConductorSerializers
    queryset=Conductor.objects.all() 

