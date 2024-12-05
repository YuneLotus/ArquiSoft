from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import filtrar_ordenes

from . import views

urlpatterns = [
    path('ordenes/', views.ordenes_list, name='ordenesList'),
    path('metodospago/', views.metodos_pago_list, name='metodospagoList'),
    path('metodopagocreate/', csrf_exempt(views.metodo_pago_create), name='metodoPagoCreate'),
    path('filtrar_ordenes/', filtrar_ordenes, name='filtrar_ordenes'),
]