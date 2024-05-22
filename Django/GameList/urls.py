from django.urls import path
from GameList import views

""" path('nombreURL',funcionVista,nombreDePagina) """
urlpatterns = [
    path("", views.index, name="index"),
    path("page2", views.page2, name="page2"),
]
