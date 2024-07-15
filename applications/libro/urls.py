from django.contrib import admin
from django.urls import path
#importando vistas
from . import views

app_name = "libros_urls"


urlpatterns = [
    path(
        'list-libros/', 
        views.ListLibro.as_view(),
        name = "TotalLibros"
    ),
]