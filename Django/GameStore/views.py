from django.shortcuts import render
from .models import Genero, Usuario
from .forms import GeneroForm,UsuarioForm

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
            "mensaje": "Registro Eliminado",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error,Rut no encontrado...",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)

def user_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        usuario = Usuario.objects.get(rut=pk)
        generos = Genero.objects.all()

        context={
            "usuario":usuario,
            "generos":generos,
        }
        return render(request,"pages/user_update.html",context)
    else:
        usuarios = Usuario.objects.all()
        context={
            "mensaje":"Error,Rut no encontrado",
            "usuarios":usuarios
        }
        return render(request,"pages/crud.html",context)

def user_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
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

        """ Obtengo genero desde la BDD para modificar """
        objGenero = Genero.objects.get(id_genero=genero)

        """ Genero la instancia """

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
        context = {
            "mensaje": "Modificado con Exito",
            "generos":generos,
            "usuario":obj,
        }
        return render(request, "pages/user_update.html", context)
 
def crud_genero(request):
    generos = Genero.objects.all()

    context={
        "generos":generos,
    }
    return render(request,"pages/crud_genero.html",context)

def genero_add(request):
    formGenero = GeneroForm()
    formUsuario = UsuarioForm()
    if request.method=="POST":
        nuevo = GeneroForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":formGenero
            }
            return render(request,"pages/genero_add.html",context)
    else:
        context = {
            "form":formGenero,
            "form2":formUsuario
        }
        return render(request,"pages/genero_add.html",context)

def genero_del(request,pk):
    try:
        genero = Genero.objects.get(id_genero=pk)
        genero.delete()

        generos = Genero.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)
    except:
        generos = Genero.objects.all()
        context={
            "mensaje":"Error, Genero no encontrado...",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)

def genero_edit(request,pk):
    if pk!="":
        genero = Genero.objects.get(id_genero=pk)
        form = GeneroForm(instance=genero)
        if request.method=="POST":
            nuevo = GeneroForm(request.POST,instance=genero)

            if nuevo.is_valid():
                nuevo.save()

                context ={
                    "mensaje":"Modificado con exito",
                    "form":nuevo
                }
                return render(request,"pages/genero_edit.html",context)
        else:
            context={
                "form":form,
            }
            return render(request,"pages/genero_edit.html",context)
    else:
        generos = Genero.objects.all()
        context={
            "mensaje":"Error, genero no encontrado",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)
