from django.db import models

#importando tabla Autor para autores = models.ManyToManyField(Autor)
from applications.autor.models import Autor


# Create your models here.

class Categoria(models.Model):
    category = models.CharField(
        "Categoria", max_length=40
    )

    """ informe admin """
    def __str__(self):
        return self.category


class Libro(models.Model):
    category = models.ForeignKey(
        Categoria, on_delete=models.CASCADE
    )
    Autores = models.ManyToManyField(Autor)
    title = models.CharField(
        "titulo", max_length=50
    )
    date = models.DateField("Fecha de lanzamieno")
    cover = models.ImageField("PILAS_AQUI", upload_to='portada', height_field=None, width_field=None, max_length=None)
    viws = models.PositiveIntegerField()
    
    """ informe admin """
    def __str__(self):
        return self.title