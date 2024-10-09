from django.contrib import admin
from .models import Colegio, Grado, Estudiante, Acudiente, Administrador

admin.site.register(Colegio)
admin.site.register(Grado)
admin.site.register(Estudiante)
admin.site.register(Acudiente)
admin.site.register(Administrador)