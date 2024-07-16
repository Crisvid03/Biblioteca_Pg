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
        #Recuperando palabra formulario nombre
        palabra_clave = self.request.GET.get("kword" , '')
        #Recuperando palabra formulario fecha 1
        f1 = self.request.GET.get("fecha1" , '')
        #Recuperando palabra formulario fecha 2
        f2 = self.request.GET.get("fecha2" , '')

        if f1 and f2 :
            return Libro.objects.listar_libros2(palabra_clave , f1 , f2)
        else :
            return Libro.objects.listar_libros(palabra_clave )

class CategoriaLibros(ListView):
    context_object_name = 'listado_libros'
    template_name = "libro/cateoria_libro.html"

    def get_queryset(self):
        return Libro.objects.libros_categorias('6')

class libroDetalle(DetailView):
    context_object_name = 'listado_libros'
    template_name = "libro/detalle_libro.html"





