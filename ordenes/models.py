from django.db import models

# Create your models here.
from instituciones.models import Estudiante, Acudiente, Colegio  # Import Estudiante model from the instituciones app
from cronogramas.models import PlantillaCronograma  # Import PlantillaCronograma model from the cronogramas app

# Orden (Order) Model
# TEMPORALMENTE SE DESCONECTA ORDEN DE ESTUDIANTE Y DE PLANTILLA, PARA FACILITAR CASO 4 Y CONSULTAS DB
class Orden(models.Model):
    # estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)  # Order is linked to a student
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Date the order was created
    fecha_vencimiento = models.DateTimeField()  # Due date for the payment
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount to be paid
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Outstanding balance
    # plantilla = models.ForeignKey(PlantillaCronograma, on_delete=models.SET_NULL, null=True, blank=True)  # Link to the template that created this order

    def __str__(self):
        return f"Orden {self.id} - {self.fecha_vencimiento}"


# Factura (Invoice) Model
class Factura(models.Model):
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)  # Invoice is linked to an guardian
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)  # Invoice is linked to an order
    fecha_pago = models.DateTimeField()  # Date the payment was made
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid
    metodo_pago = models.ForeignKey('MetodoPago', on_delete=models.SET_NULL, null=True, blank=True)  # Payment method (e.g., credit card, bank transfer)

    def __str__(self):
        return f"Factura {self.id} - Orden {self.orden.id}"

# MetodoPago (Payment Method) Model
class MetodoPago(models.Model):
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)  # Payment method is linked to a school
    nombre = models.CharField(max_length=50)  # Name of the payment method (e.g., "Credit Card")
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

# Descuento (Discount) Model
class Descuento(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)  # Discount is linked to an invoice
    descripcion = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)  # Discount percentage

    def __str__(self):
        return f"Descuento de {self.porcentaje}% para Factura {self.factura}"
