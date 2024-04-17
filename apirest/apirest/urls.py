<<<<<<< HEAD
"""importando las urls"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('docs/',include_docs_urls(title='Api documentación')),
]
=======
"""importando las urls"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path("", include("api.urls")),
    path("doc/",include_docs_urls(title='Api documentación')),
]
>>>>>>> 4adbe66a535b76c0c6e160216ebf4d0f8151c4d5
