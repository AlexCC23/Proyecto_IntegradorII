from django.db import models

# Create your models here.


class Pedido (models.Model):
    id_receta=models.CharField(max_length=8)
    id_conductor=models.CharField(max_length=8)
    id_administrador=models.CharField(max_length=8)
    estatus=models.CharField(max_length=20)
    prioridad= models.CharField(max_length=20)
    fecha=models.DateField()

