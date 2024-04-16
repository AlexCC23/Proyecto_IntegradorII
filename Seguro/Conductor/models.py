from django.db import models

# Create your models here.


class Conductor(models.Model):
    dni = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100, null=True)
    estado = models.BooleanField(default=True)
    