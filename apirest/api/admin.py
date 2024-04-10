from django.contrib import admin
from .models import Proyecto, Categoria, Comentario

# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Categoria)
admin.site.register(Comentario)