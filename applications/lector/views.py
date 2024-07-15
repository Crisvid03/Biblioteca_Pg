from django.shortcuts import render
#Importando vitas
from django.views.generic import(
    ListView,
)
#Importando Models
from .models import Lector
# Create your views here.

class ListLectores(ListView):
    context_object_name = 'listado_lectores'
    template_name = 'lector/list.html'

    def get_queryset(self):
        
        return Lector.objects.all()