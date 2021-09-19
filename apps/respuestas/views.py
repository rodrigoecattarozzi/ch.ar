from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import request
from django.contrib.auth.decorators import login_required
from .forms import Form_respuesta
from django.shortcuts import redirect, render
from .models import Respuesta
from django.contrib import messages

# Create your views here.

@login_required
def ListarRespuestas(request):
    context = {}
    listado = Respuesta.objects.all() # ORM de django
    context['respuestas'] = listado
    return render(request, 'respuestas/listadoRespuestas.html', context)

def Agregar(request):
    form = Form_respuesta(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            formulario = form.save()
            messages.success(request, 'Agregado correctamente!')
            return redirect('respuestas:listar')
    context = {
        "form": form
    }
    return render(request, 'respuestas/agregar.html', context)

def filtrarRespuesta(request):
    context = {}
    if request.GET["criterio"]:
        criterio = request.GET["criterio"]
        print(criterio)
        listado = Respuesta.objects.filter(descripcion__icontains=criterio)
        context['encontrado'] = listado
        messages.success(request, "Búsqueda finalizada!")
        return render(request,'respuestas/listadoRespuestas.html', context)
    elif request.GET["criterio"] == "":
        criterio = "Introduzca criterio de busqueda"
        listado = Respuesta.objects.all().order_by('descripcion') # ORM de django
        context['respuestas'] = listado
        return render(request, 'respuestas/listadoRespuestas.html', context)

def modificarRespuesta(request, pk):
    objeto = Respuesta.objects.filter(id = pk).first() # ORM de django
    form = Form_respuesta(request.POST or None, instance=objeto)
    if form.is_valid():
        form.save()
        return redirect('respuestas:listar')
    return render(request, 'respuestas/modificar.html', {"form": form,'objeto':objeto})

def actualizarRespuesta(request, pk):
    objeto = Respuesta.objects.get(id = pk)
    form = Form_respuesta(request.POST, instance=objeto)
    if form.is_valid():
        form.save()
    respuestas = Respuesta.objects.all()
    messages.success(request, "Actualizado Correctamente!")
    return render(request,'respuestas/listadoRespuestas.html', {"respuestas":respuestas})

def eliminarRespuesta(request, pk):
    objeto = Respuesta.objects.get(id = pk)
    objeto.delete()
    objeto = Respuesta.objects.all()
    messages.success(request, 'Selección eliminada exitosamente!')
    return render(request,'respuestas/listadoRespuestas.html', {"respuestas":objeto, "mensaje":'ok'})