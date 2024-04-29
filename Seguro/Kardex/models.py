from django.db import models

# Create your models here.

class Kardex(models.Model):
    id_medicina= models.CharField(max_length=8)
    nro_lote = models.CharField(max_length=10)
    fec_entrada = models.DateField()
    fec_venci = models.DateField() 
    cantidad = models.IntegerField()
    saldo = models.IntegerField()