from django.shortcuts import render
from .models import Genero, Usuario


# Create your views here.
def index(request):
    context = {
        "user": "",
    }
    return render(request, "pages/index.html", context)


def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "pages/crud.html", context)


def user_add(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {
            "generos": generos,
        }
        return render(request, "pages/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        objGenero = Genero.objects.get(id_genero=genero)

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/user_add.html", context)


def user_del(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
        usuario.delete()
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Eliminado con exito",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error , rut no encontrado...",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)


def user_find(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
        generos = Genero.objects.all()

        context = {
            "generos": generos,
            "usuario": usuario,
        }
        return render(request, "pages/user_edit.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "error, Rut no encontrado",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)


def user_update(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        objGenero = Genero.objects.get(id_genero=genero)

        obj = Usuario(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()
        generos = Genero.objects.all()
        usuario = Usuario.objects.get(rut=rut)
        context = {
            "generos": generos,
            "usuario": usuario,
            "mensaje": "Modificado con exito",
        }
        return render(request, "pages/user_edit.html", context)