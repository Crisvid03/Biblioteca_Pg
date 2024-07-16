from django.db import models

from django.db.models import Q

class ManagersLibro(models.Manager):
    def listar_libros(self , kword):
        resultado = self.filter(
            title__icontains = kword 
        )
        return resultado

    def listar_libros2(self , kword , fecha1 , fecha2):
        resultado = self.filter(
            title__icontains = kword ,
            date__range=(fecha1 , fecha2)
        )
        return resultado

    def libros_categorias(self , categoria):
        return self.filter(
            category__id= categoria
        ).order_by('id')

class ManagersCategoria(models.Manager):
    def categoriaAutor(self , autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinc()
