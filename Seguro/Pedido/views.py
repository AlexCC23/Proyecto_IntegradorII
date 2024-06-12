from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Pedido 
from .serializers import PedidoSerializers 


class PedidoView(viewsets.ModelViewSet):
    serializer_class=PedidoSerializers
    queryset=Pedido.objects.all() 

class PedidoForPrioridadView(viewsets.ViewSet):
    def list(self, request, prio,fec,cond,sta):
        queryset = Pedido.objects.filter(fecha=fec,prioridad=prio,id_conductor=cond,estatus=sta)
        serializer = PedidoSerializers(queryset, many=True)
        return Response(serializer.data)
    
class PedidoForConductor(viewsets.ViewSet):
    def list(self, request,prio,fec,cond):
        queryset = Pedido.objects.filter(fecha=fec,prioridad=prio,id_conductor=cond)
        serializer = PedidoSerializers(queryset, many=True)
        return Response(serializer.data)
    