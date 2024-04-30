from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Pedido 
from .serializers import PedidoSerializers 


class PedidoView(viewsets.ModelViewSet):
    serializer_class=PedidoSerializers
    queryset=Pedido.objects.all() 
