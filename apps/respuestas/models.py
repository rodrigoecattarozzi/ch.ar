from django.db import models
from apps.core.models import TimeModels
from apps.preguntas.models import Pregunta

class Respuesta(TimeModels):
	pregunta = models.ForeignKey(Pregunta, related_name = 'mi_pregunta', on_delete = models.CASCADE)
	descripcion = models.CharField(max_length = 255)
	correcta = models.BooleanField(default = False)
	seleccionada = models.BooleanField(default = False)

	def __str__(self):
		return self.descripcion



