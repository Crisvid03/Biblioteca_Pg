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
from .models import Libro

# Create your views here.

class ListLibro(ListView):
    context_object_name = 'listado_libros'
    template_name = 'libro/list.html'

    def get_queryset(self):

        return Libro.objects.all()




