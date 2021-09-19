from io import IOBase
from django import forms
from django.contrib import messages
from django.http import request, HttpResponse
from .forms import Form_pregunta
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from .models import Pregunta
from django.template.loader import render_to_string

# Create your views here.

@login_required
def ListarPreguntas(request):
    context = {}
    listado = Pregunta.objects.all().order_by('descripcion') # ORM de django
    context['preguntas'] = listado
    return render(request, 'preguntas/listarPreguntas.html', context)

@login_required
def AsignarRespuestas(request, pk):
    context = {}
    #SELECT * FROM PRODUCTOS WHERE id = pk
    objeto = Pregunta.objects.get(id = pk) # ORM de django
    print(objeto)
    context['pregunta'] = objeto
    return render(request, 'respuestas/listadoRespuestas.html', context)

@login_required
def Agregar(request):
    form = Form_pregunta(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            formulario = form.save()
            messages.success(request, "Creado correctamente!")
            return redirect('preguntas:listar')
    context = {
        "form": form
    }
    return render(request, 'preguntas/agregar.html', context)

@login_required
def filtrarPregunta(request):
    context = {}
    if request.GET["criterio"]:
        criterio = request.GET["criterio"]
        print(criterio)
        listado = Pregunta.objects.filter(descripcion__icontains=criterio)
        context['encontrado'] = listado
        messages.success(request, "Búsqueda finalizada!")
        return render(request,'preguntas/listarPreguntas.html', context)
    elif request.GET["criterio"] == "":
        #criterio = "Introduzca criterio de busqueda"
        listado = Pregunta.objects.all().order_by('descripcion') # ORM de django
        context['preguntas'] = listado
        return render(request, 'preguntas/listarPreguntas.html', context)

@login_required
def modificarPregunta(request, pk):
    objeto = Pregunta.objects.filter(id = pk).first() # ORM de django
    form = Form_pregunta(instance=objeto)
    return render(request, 'preguntas/modificar.html', {"form": form,'objeto':objeto})

def actualizarPregunta(request, pk):
    objeto = Pregunta.objects.get(id = pk)
    form = Form_pregunta(request.POST, instance=objeto)
    if form.is_valid():
        form.save()
    preguntas = Pregunta.objects.all()
    messages.success(request, "Actualizado Correctamente!")
    return render(request,'preguntas/listarPreguntas.html', {"preguntas":preguntas, "mensaje":'ok'})
    

@login_required
def eliminarPregunta(request, pk):
    objeto = Pregunta.objects.get(id = pk)
    objeto.delete()
    objeto = Pregunta.objects.all()
    messages.success(request, 'Selección eliminada exitosamente!')
    return render(request,'preguntas/listarPreguntas.html', {"preguntas":objeto, "mensaje":'ok'})