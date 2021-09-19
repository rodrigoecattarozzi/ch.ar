from django.urls import path, include
from .import views

app_name = 'partidas'


urlpatterns = [
  path('jugar/', views.mostrarPregunta, name='jugar'),
  path('ranking/', views.ranking, name='ranking'),
  path('misPartidas/<int:pk>', views.misPartidas, name='misPartidas'),
  path('seleccionarCategoria/', views.seleccionarCategoria, name='seleccionarCategoria'),
  path('mostrarPregunta/<int:pk>', views.mostrarPregunta, name='mostrarPregunta'),
  path('mostrarResultado/<int:pk>', views.mostrarResultado, name='mostrarResultado'),
]