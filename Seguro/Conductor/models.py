from django.db import models

# Create your models here.


class Conductor(models.Model):
    dni = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    licencia = models.CharField(max_length=10)
    placa = models.CharField(max_length=15)
    Latitud=models.CharField(max_length=200, null=True)
    Longitud=models.CharField(max_length=200, null=True)
    estado = models.BooleanField(default=True)
    #cada vez que se actuliza los parametros se ejecutan los dos  comandos