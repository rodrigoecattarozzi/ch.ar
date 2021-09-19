from django import forms
from django.forms import ModelForm
#from bootstrap_modal_forms.forms import BSModalModelForm
from django.http import request
from .models import Respuesta

class Form_respuesta(ModelForm):
    class Meta:
        model = Respuesta
        fields = ['descripcion', 'pregunta', 'correcta']





