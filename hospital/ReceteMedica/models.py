from django.db import models

class Receta(models.Model):
    dni_Paciente=models.CharField(max_length=8)
    nombre_Medico=models.CharField(max_length=150)
    fecha=models.DateField(auto_now_add=True)
    hora=models.TimeField(auto_now_add=True)
    prioridad = models.CharField(max_length=20)

    
