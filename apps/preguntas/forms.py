from django.forms import ModelForm
from django.http import request
from .models import Pregunta

class Form_pregunta(ModelForm):
    class Meta:
        model = Pregunta
        fields = ['categoria', 'descripcion']

#https://pypi.org/project/django-bootstrap-modal-forms/


