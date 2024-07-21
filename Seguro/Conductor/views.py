from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Conductor 
from .serializers import ConductorSerializers 


class ConductorView(viewsets.ModelViewSet):
    serializer_class=ConductorSerializers
    queryset=Conductor.objects.all() 

class ConductorDireccionView(viewsets.ViewSet):
    def list(self, request,direc):
        queryset = Conductor.objects.filter(direccion =direc )
        serializer = ConductorSerializers(queryset, many=True)
        return Response(serializer.data)