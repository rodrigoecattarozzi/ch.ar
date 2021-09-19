from django.forms import ModelForm
from django.http import request
from .models import Categoria

class Form_categoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','descripcion','color','icono']
