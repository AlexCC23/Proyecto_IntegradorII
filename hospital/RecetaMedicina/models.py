from django.db import models

# Create your models here.

class RecetaMedicina(models.Model):
    id_receta=models.CharField(max_length=10)
    id_medicina=models.CharField(max_length=10)
    cantidad=models.IntegerField()
    description=models.TextField()
