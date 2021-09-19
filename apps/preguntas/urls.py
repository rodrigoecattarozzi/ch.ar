from django.urls import path, include
from .import views

app_name = 'preguntas'

urlpatterns = [
  path('crear/', views.Agregar, name='crear'),
  path('listar/', views.ListarPreguntas, name='listar'),
  path('buscar/', views.filtrarPregunta, name='buscar'),
  path('modificar/<int:pk>', views.modificarPregunta, name='modificar'),
  path('actualizar/<int:pk>', views.actualizarPregunta, name='actualizar'),
  path('eliminar/<int:pk>', views.eliminarPregunta, name='eliminar'),
]