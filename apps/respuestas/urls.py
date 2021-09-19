from django.urls import path, include
from .import views

app_name = 'respuestas'

urlpatterns = [
  path('crear/', views.Agregar, name='crear'),
  path('listar/', views.ListarRespuestas, name='listar'),
  path('buscar/', views.filtrarRespuesta, name='buscar'),
  path('modificar/<int:pk>', views.modificarRespuesta, name='modificar'),
  path('actualizar/<int:pk>', views.actualizarRespuesta, name='actualizar'),
  path('eliminar/<int:pk>', views.eliminarRespuesta, name='eliminar'),
]