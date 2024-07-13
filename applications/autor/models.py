from django.db import models

# Create your models here.

class Autor(models.Model):
    
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