from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Pedido 
from .serializers import PedidoSerializers 

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import PyPDF2
from io import BytesIO
from django.http import HttpResponse

import os
import resend
from .serializers import EmailSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .serializers import SMSSerializer
import vonage


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
    
class PedidoForReceta(viewsets.ViewSet):
    def list(self, request,est,rec):
        queryset = Pedido.objects.filter(estatus=est,id_receta=rec)
        serializer = PedidoSerializers(queryset, many=True)
        return Response(serializer.data)  
    

class AddPasswordToPdf(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        user_password = request.data['user_password']
        owner_password = request.data['owner_password']

        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(user_password, owner_password)

        buffer = BytesIO()
        pdf_writer.write(buffer)
        buffer.seek(0)

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="encrypted.pdf"'
        return response
    
class SendEmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            dni = serializer.validated_data['dni']
            email = serializer.validated_data['email']
            pdf1 = serializer.validated_data['pdf1']
            pdf2 = serializer.validated_data['pdf2']

            resend.api_key = "re_C7tBrtpf_EVmP6C85GA3rwCkpyHa4giFn"

            # Guardar los PDFs temporalmente
            path1 = default_storage.save('temp1.pdf', ContentFile(pdf1.read()))
            full_path1 = os.path.join(default_storage.location, path1)

            path2 = default_storage.save('temp2.pdf', ContentFile(pdf2.read()))
            full_path2 = os.path.join(default_storage.location, path2)

            # Leer el contenido de los archivos PDF
            with open(full_path1, "rb") as f1:
                pdf_content1 = f1.read()

            with open(full_path2, "rb") as f2:
                pdf_content2 = f2.read()

            # Convertir el contenido a una lista de bytes
            pdf_bytes_list1 = list(pdf_content1)
            pdf_bytes_list2 = list(pdf_content2)
            
            html_content = f"""
                <p>Estimado/a {name}, con el dni: {dni}</p>
                <p>Le agradecemos por elegir nuestros servicios. Adjuntamos su boleta y la guia de remision.</p>
                <p>En HEALTH EXPRESS, nos comprometemos a brindarle un servicio rápido, confiable y seguro para satisfacer todas sus necesidades de salud.</p>
                <p>Atentamente,</p>
                <p>El equipo de HEALTH EXPRESS</p>
            """

            # Preparar los datos para el correo
            attachment1 = {"filename": "boleta.pdf", "content": pdf_bytes_list1}
            attachment2 = {"filename": "GuiaRemision.pdf", "content": pdf_bytes_list2}

            params: resend.Emails.SendParams = {
                "from": "HEALTH EXPRESS <HEALTHEXPRESS@resend.dev>",
                "to": [email],
                "subject": name,
                "html": html_content,
                "attachments": [attachment1, attachment2],
            }

            response = resend.Emails.send(params)

            # Eliminar los archivos temporales
            default_storage.delete(full_path1)
            default_storage.delete(full_path2)
            
            return Response({'message': response}, status=status.HTTP_200_OK)
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class SendSMS(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SMSSerializer(data=request.data)
        if serializer.is_valid():
            to = serializer.validated_data['to']
            text = serializer.validated_data['text']

            # Configura el cliente de Vonage
            client = vonage.Client(key="c376f0e5", secret="i90HLuGP2hq6cetR")
            sms = vonage.Sms(client)

            responseData = sms.send_message({
                "from": "HeltExpes",
                "to": to,
                "text": text,
            })

            if responseData["messages"][0]["status"] == "0":
                return Response({"message": "SMS enviado exitosamente"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Error al enviar SMS"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)