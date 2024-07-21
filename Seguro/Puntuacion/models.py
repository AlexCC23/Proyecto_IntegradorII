from django.db import models

# Create your models here.

class Puntuacion(models.Model):
    id_pedido = models.CharField(max_length=10)
    puntuacion= models.IntegerField()
    id_conductor= models.CharField(max_length=8)
    
