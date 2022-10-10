from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from clientes.views import ClientesViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
