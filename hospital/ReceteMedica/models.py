from django.db import models

class Receta(models.Model):
    dni_Paciente=models.CharField(max_length=10)
    nombre_Medico=models.CharField(max_length=150)
    
