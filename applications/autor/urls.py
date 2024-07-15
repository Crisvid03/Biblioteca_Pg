from django.contrib import admin
from django.urls import path
#importando vistas
from . import views

app_name = "autor_urls"


urlpatterns = [
    path(
        'list-autores/', 
        views.ListAutores.as_view(),
        name = "TotalAutores"
    ),
]
