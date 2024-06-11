from django import forms
from .models import Genero, Usuario

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"