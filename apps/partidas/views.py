from django.shortcuts import render
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http.response import HttpResponse
from django.urls import reverse_lazy
#from bootstrap_modal_forms.generic import BSModalCreateView
from .models import Partida
#from .forms import SeleccionarRespuestas
from apps.categorias.models import Categoria
from django.contrib.auth.models import User
from apps.preguntas.models import Pregunta
from apps.respuestas.models import Respuesta
import random

# Create your views here.

@login_required
def ranking(request):
	context ={}
	rank = Partida.objects.order_by('-puntaje')[:50]
	context['ranking'] = rank
	return render(request, 'partidas/ranking.html', context)

@login_required
def misPartidas(request, pk):
	context ={}
	partida = Partida.objects.filter(usuario_id = pk)
	context['partidas'] = partida
	return render(request, 'partidas/misPartidas.html', context)

@login_required
def seleccionarCategoria(request):
	context ={}
	categoria = Categoria.objects.all()
	context['categorias'] = categoria
	return render(request, 'partidas/seleccionarCategoria.html', context)

@login_required
def mostrarPregunta(request, pk):

	categoria = Categoria.objects.get(pk=pk)
	partida = Partida.objects.filter(categoria = categoria, usuario=request.user, finalizada=False).last()
	if not partida:
		partida = Partida()
		partida.usuario = request.user
		partida.categoria = categoria
		partida.save()
	
	
	if partida.contador <= 5:
		contador = partida.contador
		partida.contador = contador + 1
		partida.save()
		contador = partida.contador
		pregunta = Pregunta.objects.filter(mostrada = False, categoria_id = pk).order_by("?").first()
		if pregunta:
			pregunta.mostrada=True
			pregunta.save()
		else:
			pregunta = Pregunta.objects.filter(categoria_id = pk).order_by("?").first()
		
		respuestas = Respuesta.objects.filter(pregunta_id=pregunta.id)
		context={'categoria': categoria, 'pregunta': pregunta, 'respuesta': respuestas}
		return render(request, 'partidas/mostrarPregunta.html', context)
	else:
		contador = True
		contexto = {'contador': contador}
		partida.finalizada = True
		partida.save()
		return render(request, 'partidas/mostrarPregunta.html', contexto)

@login_required
def mostrarResultado(request, pk):
	if request.method=="POST":
		seleccion = []
		pregunta = Pregunta.objects.get(pk=pk)
		categoria = pregunta.categoria
		partida = Partida.objects.filter(categoria = categoria).last()
		id_partida = partida.id
		for i in request.POST:
			if i != "csrfmiddlewaretoken":
				seleccion.append(i)
		for s in seleccion:
			respuesta=Respuesta.objects.filter(id=int(s)).update(seleccionada=True)
		correctas = (Respuesta.objects.filter(pregunta_id = pk, correcta=True, seleccionada=True)).count()
		print(correctas)
		incorrectas = (Respuesta.objects.filter(pregunta_id = pk, correcta=False, seleccionada=True)).count()
		print(incorrectas)
		total = correctas - incorrectas
		if (total < 0):
			total = 0
		total = total + partida.puntaje
		partida.puntaje = total
		partida.save()
		puntaje = partida.puntaje
		respuestas_seleccionadas=[]
		for s in seleccion:
			respuestas_seleccionadas.append(Respuesta.objects.get(id=int(s)))
		id_respuesta = int(seleccion[0])
		pregunta = Respuesta.objects.get(id=id_respuesta)
		id_pregunta = pregunta.pregunta_id
		cat = Pregunta.objects.get(id=id_pregunta)
		context={'puntaje': puntaje, 'respuestas_seleccionadas': respuestas_seleccionadas, 'categoria': categoria.id}
		return render(request, 'partidas/mostrarResultado.html', context)
	else:
		return render(request, 'partidas/mostrarResultado.html')

