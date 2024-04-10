"""importando los modelos"""

from django.db import models


class Categoria(models.Model):
    """categoria a la que pertenece cada proyecto"""

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    """Modelo del proyecto"""

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    url = models.URLField(blank=False, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    """Aca los comentarios acerca del proyecto"""

    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, related_name="comentarios"
    )
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario en {self.proyecto}: {self.texto[:50]}..."
