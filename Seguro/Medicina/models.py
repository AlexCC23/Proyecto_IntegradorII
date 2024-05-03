from django.db import models

# Create your models here.

class Medicina(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2,max_digits=6)
                                   