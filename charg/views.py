from django.shortcuts import render
from django.contrib import messages


def Home(request):
	return render(request, 'home.html')

def Nosotros(request):
	return render(request, 'nosotros.html')

def comoJugar(request):
	return render(request, 'como-jugar.html')

