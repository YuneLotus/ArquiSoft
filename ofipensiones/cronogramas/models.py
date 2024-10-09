from django.db import models
from instituciones.models import Colegio, Estudiante  # Import models from instituciones app


class Cronograma(models.Model):
    concepto = models.CharField(max_length=100)  # Name of the schedule (e.g., "Cronograma 6B-2024")
    descripcion = models.TextField(null=True, blank=True)  # Description of the schedule
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)  # The schedule belongs to a school
    estudiantes = models.ManyToManyField(Estudiante, related_name='cronogramas')  # Schedule is linked to students

    def __str__(self):
        return self.concepto
    
class PlantillaCronograma(models.Model):
    nombre = models.CharField(max_length=100)  # Name of the template (e.g., "Tuition January 2024")
    descripcion = models.TextField(null=True, blank=True)  # Description of the template
    fecha_desde = models.DateTimeField()  # Start date for the charge
    fecha_hasta = models.DateTimeField()  # End date (deadline) for the charge
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # The amount to be charged
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, related_name="plantillas")  # Template belongs to a schedule

    def __str__(self):
        return f"{self.nombre} ({self.fecha_desde} - {self.fecha_hasta})"
