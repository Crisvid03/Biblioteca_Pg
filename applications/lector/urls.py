from django.contrib import admin
from django.urls import path
#importando vistas
from . import views

app_name = "lectores_urls"


urlpatterns = [
    path(
        'list-lectores/', 
        views.ListLectores.as_view(),
        name = "TotalLectores"
    ),
]
