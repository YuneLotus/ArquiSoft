from django.db import models

# Create your models here.
class Colegio(models.Model):
    nit = models.IntegerField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Grado(models.Model):
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)  # Each grade belongs to a school
    codigo = models.CharField(unique=True, primary_key=True, max_length=50) # like 6B-2020
    grado = models.CharField(max_length=50) 
    grupo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    jornada = models.CharField(max_length=50)  # Schedule (morning or afternoon classes)

    def __str__(self):
        return f"{self.grado} - {self.grupo}"
    
class Estudiante(models.Model):
    codigo = models.IntegerField(unique=True, primary_key=True)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    acudientes = models.ManyToManyField('Acudiente', related_name='estudiantes')  # Many-to-many relationship

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Acudiente(models.Model):
    cedula = models.IntegerField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Administrador(models.Model):
    cedula = models.IntegerField(unique=True, primary_key=True)  
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)  # Role or position

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"
    
