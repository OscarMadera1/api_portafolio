from rest_framework import viewsets
from .serealaizer import (
    Proyectoserialaizer,
    Categoriaserialaizer,
    Comentariooserialaizer,
)
from .models import Proyecto, Categoria, Comentario

# Create your views here.


class Proyectoviewset(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = Proyectoserialaizer


class Categoriaviewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = Categoriaserialaizer


class Comentarioviewset(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = Comentariooserialaizer
