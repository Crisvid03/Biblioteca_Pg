from django.db import models

#importando tabla Autor para autores = models.ManyToManyField(Autor)
from applications.autor.models import Autor

#importando managers
from .managers import (
    ManagersLibro , 
    ManagersCategoria
)

# Create your models here.

class Categoria(models.Model):
    category = models.CharField(
        "Categoria", max_length=40
    )

    objects = ManagersCategoria()

    """ informe admin """
    def __str__(self):
        return  str(self.id) + "-" + self.category


class Libro(models.Model):
    category = models.ForeignKey(
        Categoria, on_delete=models.CASCADE ,
        related_name='categoria_libro'
    )
    autores = models.ManyToManyField(Autor)
    title = models.CharField(
        "titulo", max_length=50
    )
    date = models.DateField("Fecha de lanzamieno")
    cover = models.ImageField("Portada", 
        upload_to='portada', 
        blank=True,
        null = True
    )
    viws = models.PositiveIntegerField(
        blank=True,
        null = True
    )

    objects = ManagersLibro()
    
    """ informe admin """
    def __str__(self):
        return  str(self.id) + "-" + self.title