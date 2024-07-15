from django.db import models

class AutorManager(models.Manager):

    def listarAutores(self):
        return self.all()