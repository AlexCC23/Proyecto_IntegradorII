from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Medicina 
from .serializers import MedicinaSerializers 


class MedicinaView(viewsets.ModelViewSet):
    serializer_class=MedicinaSerializers
    queryset=Medicina.objects.all() 
