from .models import Categoria
from .forms import Form_categoria
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import request
from django.contrib import messages
# Create your views here.

@login_required
def ListarCategorias(request):
    context = {}
    listado = Categoria.objects.all() # ORM de django
    context['categorias'] = listado
    return render(request, 'categorias/listadoCategoria.html', context)

def Agregar(request):
    form = Form_categoria(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            formulario = form.save()
            messages.success(request, "Creado correctamente!")
            return redirect('categorias:listar')
    context = {
        "form": form
    }
    return render(request, 'categorias/agregar.html', context)

def filtrarCategoria(request):
    context = {}
    if request.GET["criterio"]:
        criterio = request.GET["criterio"]
        print(criterio)
        listado = Categoria.objects.filter(nombre__icontains=criterio)
        context['encontrado'] = listado
        messages.success(request, "Búsqueda finalizada!")
        return render(request,'categorias/listadoCategoria.html', context)
    elif request.GET["criterio"] == "":
        criterio = "Introduzca criterio de búsqueda"
        listado = Categoria.objects.all().order_by('nombre') # ORM de django
        context['categorias'] = listado
        return render(request, 'categorias/listadoCategoria.html', context)

def modificarCategoria(request, pk):
    objeto = Categoria.objects.filter(id = pk).first() # ORM de django
    form = Form_categoria(instance=objeto)
    return render(request, 'categorias/modificar.html', {"form": form,'objeto':objeto})

def actualizarCategoria(request, pk):
    objeto = Categoria.objects.get(id = pk)
    form = Form_categoria(request.POST, instance=objeto)
    if form.is_valid():
        form.save()
    categorias = Categoria.objects.all()
    messages.success(request, "Actualizado Correctamente!")
    return render(request,'categorias/listadoCategoria.html', {"categorias":categorias})

def eliminarCategoria(request, pk):
    objeto = Categoria.objects.get(id = pk)
    objeto.delete()
    objeto = Categoria.objects.all()
    messages.success(request, 'Selección eliminada exitosamente!')
    return render(request,'categorias/listadoCategoria.html', {"categorias":objeto, "mensaje":'ok'})