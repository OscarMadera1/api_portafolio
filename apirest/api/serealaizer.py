from rest_framework import serializers
from .models import Proyecto, Categoria, Comentario


class Proyectoserialaizer(serializers.ModelSerializer):
    """Serializador de modelo proyecto"""

    class Meta:
        model = Proyecto
        fields = "__all__"


class Categoriaserialaizer(serializers.ModelSerializer):
    """Serializador de modelo categoria"""

    class Meta:
        model = Categoria
        fields = "__all__"


class Comentariooserialaizer(serializers.ModelSerializer):
    """Serializador de modelo comentario"""

    class Meta:
        model = Comentario
        fields = "__all__"
