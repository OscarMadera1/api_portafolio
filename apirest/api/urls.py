from .views import Proyectoviewset, Categoriaviewset, Comentarioviewset
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"proyecto", Proyectoviewset)
router.register(r"categoria", Categoriaviewset)
router.register(r"comentario", Comentarioviewset)
urlpatterns = [path("", include(router.urls))]
