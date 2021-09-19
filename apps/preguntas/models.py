from django.db import models
from django.forms.models import ModelForm
from apps.core.models import TimeModels
from apps.categorias.models import Categoria

class Pregunta(TimeModels):
	categoria = models.ForeignKey(Categoria, related_name = 'mi_categoria', on_delete = models.CASCADE)
	descripcion = models.CharField(max_length = 255)
	mostrada = models.BooleanField(default = False)

	def __str__(self):
		return self.descripcion

