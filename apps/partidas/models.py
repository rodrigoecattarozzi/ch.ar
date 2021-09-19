from django.db import models
from apps.core.models import TimeModels
from django.contrib.auth.models import User
from apps.categorias.models import Categoria

class Partida(TimeModels):
	usuario = models.ForeignKey(User, related_name = 'mi_usuario', on_delete = models.CASCADE)
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, default = 0)
	puntaje = models.IntegerField(default = 0)
	finalizada = models.BooleanField(default = False)
	contador = models.IntegerField(default = 1)
	max_preguntas = models.IntegerField(default = 5)

	def __str__(self):
		return str(self.puntaje)