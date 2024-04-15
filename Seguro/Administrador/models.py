from django.db import models

# Create your models here.

class Administrador(models.Model):
    dni = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

   