from django import forms
from .models import Categoria, Proyecto, Comentario


class CategoriaForm(forms.ModelForm):
    """Formulario"""
    class Meta:
        model = Categoria
        fields = "__all__"

class ProyectoForm(forms.ModelForm):
    """Formulario"""
    class Meta:
        model = Proyecto
        exclude = ['fecha_creacion']

class ComentarioForm(forms.ModelForm):
    """Formulario"""
    class Meta:
        model = Comentario
        exclude = ['fecha_creacion']