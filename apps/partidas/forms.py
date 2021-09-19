# from django.forms import ModelForm
# from django import forms
# from django.http import request
# from apps.respuestas.models import Respuesta

# class SeleccionRespuestas(forms.Form):
#     respuestas = forms.MultipleChoiceField(
#         seleccion = Respuesta.objects.filter(pregunta_id=self.pk),
#         widget  = forms.CheckboxSelectMultiple,
#     )

#     def __init__(self, pk):
#         return pk