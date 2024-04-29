from django.db import models

# Create your models here.

class Receta(models.Model):
    dni_asegurado = models.CharField(max_length=8)
    fecha = models.DateField()
    nom_doctor = models.CharField(max_length=50)
    co_pago=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    