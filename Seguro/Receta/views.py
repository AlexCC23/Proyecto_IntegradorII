from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Receta 
from .serializers import RecetaSerializers 


class RecetaView(viewsets.ModelViewSet):
    serializer_class=RecetaSerializers
    queryset=Receta.objects.all() 
    
class RecetaForIDView(viewsets.ViewSet):
    def list(self, request, id):
        queryset = Receta.objects.filter(id_receta=id)
        serializer = RecetaSerializers(queryset, many=True)
        return Response(serializer.data)