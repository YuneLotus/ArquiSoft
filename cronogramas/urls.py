from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('cronogramas/', views.cronogramas_list, name='cronogramasList'),
    path('cronogramacreate/', csrf_exempt(views.cronograma_create), name='cronogramaCreate'),
]