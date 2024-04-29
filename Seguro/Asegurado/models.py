from django.db import models

# Create your models here.

class Asegurado(models.Model):
    dni = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100,null=True)
    ubicacion = models.CharField(max_length=100)
    TipoSeguro= models.CharField(max_length=50, default="")
    contraseña = models.CharField(max_length=100,null=True)