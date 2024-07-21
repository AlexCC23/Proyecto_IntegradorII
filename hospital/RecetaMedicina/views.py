from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import RecetaMedicina 
from .serializers import RecetaMedicinaSerializers 


class RecetaMedicinaView(viewsets.ModelViewSet):
    serializer_class=RecetaMedicinaSerializers
    queryset=RecetaMedicina.objects.all() 
    
    
class RecetaDetalleView(viewsets.ViewSet):
    def list(self, request,rec):
        queryset = RecetaMedicina.objects.filter(id_receta=rec)
        serializer = RecetaMedicinaSerializers(queryset, many=True)
        return Response(serializer.data)