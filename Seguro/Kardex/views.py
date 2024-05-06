from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Kardex 
from .serializers import KardexSerializers 


class KardexView(viewsets.ModelViewSet):
    serializer_class=KardexSerializers
    queryset=Kardex.objects.all() 
    
class KardexMedicinaView(viewsets.ViewSet):
    def list(self, request,med):
        queryset = Kardex.objects.filter(id_medicina=med)
        serializer = KardexSerializers(queryset, many=True)
        return Response(serializer.data)