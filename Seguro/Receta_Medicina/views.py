from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Receta_Medicina 
from .serializers import Receta_MedicinaSerializers 


class Receta_MedicinaView(viewsets.ModelViewSet):
    serializer_class=Receta_MedicinaSerializers
    queryset=Receta_Medicina.objects.all() 
    
    
    
class RecetaIDMedicinaView(viewsets.ViewSet):
    def list(self, request, id_rec):
        queryset = Receta_Medicina.objects.filter(id_receta=id_rec);
        serializer = Receta_MedicinaSerializers(queryset, many=True)
        return Response(serializer.data)
    