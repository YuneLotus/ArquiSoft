from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('metodospago/', views.metodos_pago_list, name='metodospagoList'),
    path('metodopagocreate/', csrf_exempt(views.metodo_pago_create), name='metodoPagoCreate'),
]