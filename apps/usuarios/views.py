from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuario creado')
            return redirect("usuarios:login")
    contexto = {
        "form":form
    }
    return render(request,"usuarios/register.html",contexto)

def perfil(request, id):
    user = User.objects.get(pk=id)
    contexto = {
        "usuario":user
    }
    return render(request, "usuarios/perfil.html", contexto)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect("usuarios:login")

    perfil = request.user
    form = EditProfileForm(instance=perfil)
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=perfil)
        if form.is_valid():
            user = form.save()
            return redirect("home")
    contexto = {"form":form}
    return render(request, "usuarios/edit.html",contexto)



# def listar_usuarios(request):
#     return HttpResponse("listado de usuarios")
# def crear_usuario(request):
#     return HttpResponse("crear usuario")
# def ver_usuario(request, id):
#     return HttpResponse(f"ver usuario {id}")
# def modificar_usuario(request, id):
#     return HttpResponse(f"modificar usuario {id}")
# def eliminar_usuario(request, id):
#     return HttpResponse(f"eliminar usuario {id}")

