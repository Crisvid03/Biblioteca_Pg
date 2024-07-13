from django.db import models

from applications.libro.models import Libro
# Create your models here.

class Lector(models.Model):
    name = models.CharField(
        "Nombre", max_length=50
    )
    last_name = models.CharField(
        "Apellido", max_length=50
    )
    country = models.CharField(
        "Nacionalidad", max_length=50
    )
    old = models.PositiveIntegerField()

    """ informe admin """
    def __str__(self):
        return self.name + '-' + self.last_name

class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector, 
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE
    )
    fecha_prestamo = models.DateField("fecha de salida")
    fecha_devolucion = models.DateField(
        blank=True,
        null = True
    )
    entregado = models.BooleanField()

    def __str__(self):
        return self.libro.title
