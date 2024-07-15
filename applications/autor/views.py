from django.shortcuts import render
#Importanto el tipo de vistas
from django.views.generic import(
        ListView , 
        DetailView,
        CreateView,
        TemplateView,
        UpdateView,
        DeleteView,
        FormView,
    )
#Importando models
from .models import Autor

# Create your views here.

class ListAutores(ListView):
    context_object_name = 'listado_autores'
    template_name = 'autor/list.html'

    def get_queryset(self):

        return Autor.objects.listarAutores()