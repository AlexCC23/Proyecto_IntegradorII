from django.db import models

# Create your models here.

class Receta_Medicina(models.Model):
    id_receta = models.CharField(max_length=8)
    id_medicina = models.CharField(max_length=8)
    cantidad =  models.IntegerField()
    descripcion = models.TextField()
