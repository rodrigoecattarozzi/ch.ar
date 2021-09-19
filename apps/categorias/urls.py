from django.urls import path
from .import views

app_name = 'categorias'

urlpatterns = [
  path('crear/', views.Agregar, name='crear'),
  path('listar/', views.ListarCategorias, name='listar'),
  path('buscar/', views.filtrarCategoria, name='buscar'),
  path('modificar/<int:pk>', views.modificarCategoria, name='modificar'),
  path('actualizar/<int:pk>', views.actualizarCategoria, name='actualizar'),
  path('eliminar/<int:pk>', views.eliminarCategoria, name='eliminar'),

  #path('Asignar/<int:pk>', views.AsignarRespuestas, name='asignar'),
]