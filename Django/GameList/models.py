from django.db import models


# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column="idGenero", primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey(
        "Genero", on_delete=models.CASCADE, db_column="idGenero"
    )
    telefono = models.CharField(max_length=12)
    edad = models.IntegerField()
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField()

    def __str__(self):
        return (
            str(self.nombre)
            + " "
            + str(self.apellido_paterno)
            + " "
            + str(self.apellido_materno)
        )
