from django.db import models
from apps.core.models import TimeModels

class Categoria(TimeModels):
	nombre = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 50, null = True)
	color = models.CharField(max_length = 6)
	icono = models.CharField(max_length = 25)
	
	def __str__(self):
		return self.nombre
