from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('colegios/', views.colegios_list, name='colegioList'),

]