from django.shortcuts import render
from .models import Genero, Usuario


# Create your views here.
def index(request):
    """context: paquete variables que pueden ser consumidas por el front"""
    context = {
        "usuario": "Jose Riquelme",
        "carrito": [],
    }
    return render(request, "pages/index.html", context)


def page2(request):
    """traer todos los usuarios de la BDD"""
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "pages/page2.html", context)


def page3(request):
    context = {}
    return render(request, "pages/actividadCSS.html", context)
