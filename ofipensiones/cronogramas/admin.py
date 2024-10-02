from django.contrib import admin

# Register your models here.
from .models import Cronograma, PlantillaCronograma

admin.site.register(Cronograma)
admin.site.register(PlantillaCronograma)