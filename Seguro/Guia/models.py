from django.db import models

# Create your models here.

class Guia(models.Model):
    id_pedido = models.CharField(max_length=9)
    fecha = models.DateField(auto_now_add=True) 