from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('colegios/', views.colegios_list, name='colegioList'),
    path('grados/', views.grados_list, name='gradosList'),
    path('gradocreate/', csrf_exempt(views.grado_create), name='gradoCreate'),
    path('acudientes/', views.acudientes_list, name='acudientesList'),
    path('estudiantes/', views.estudiantes_list, name='estudiantesList'),
    path('estudiantecreate/', csrf_exempt(views.estudiante_create), name='estudianteCreate'),
]