from django.db import models

#importando para q haga la comparacion OR
from django.db.models import Q

class AutorManager(models.Manager):

    def buscar_autor(self , kword):
        resultado = self.filter(name__icontains=kword)
        return resultado

    def buscar_autor2(self , kword):
        resultado = self.filter(
            Q(name__icontains=kword) | Q(last_name__icontains=kword)
        )
        return resultado