from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Guia 
from .serializers import GuiaSerializers 


class GuiaView(viewsets.ModelViewSet):
    serializer_class=GuiaSerializers
    queryset=Guia.objects.all() 

class GuiaForPedidoView(viewsets.ViewSet):
    def list(self, request, pedi):
        queryset = Guia.objects.filter(id_pedido=pedi)
        serializer = GuiaSerializers(queryset, many=True)
        return Response(serializer.data)