from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', inventario, name='inventario'),
    path('eliminar/<int:id>', eliminar, name='eliminar'),
    path('editar/<int:id>', editar, name='editar'),
    path('addcategoria', add_categoria, name='addcategoria'),
    path('addproveedor', add_proveedor, name='addproveedor'),
]
