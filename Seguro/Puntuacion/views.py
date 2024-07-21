from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Puntuacion 
from .serializers import PuntuacionSerializers 


class PuntuacionView(viewsets.ModelViewSet):
    serializer_class=PuntuacionSerializers
    queryset=Puntuacion.objects.all() 

class PuntuacionForPedidoView(viewsets.ViewSet):
    def list(self, request, pedi):
        queryset = Puntuacion.objects.filter(id_pedido=pedi)
        serializer = PuntuacionSerializers(queryset, many=True)
        return Response(serializer.data)
    
class PuntuacionForConductorView(viewsets.ViewSet):
    def list(self, request, cond):
        queryset = Puntuacion.objects.filter(id_conductor=cond)
        serializer = PuntuacionSerializers(queryset, many=True)
        return Response(serializer.data)   
