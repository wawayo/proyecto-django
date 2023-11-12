from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
# Create your views here.

def welcome_view(request):
    return render(request, 'Recetario/welcome.html')

def recetas_view(request):
    recetas = Receta.objects.all()
    return render(request, 'Recetario/recetas.html', {'recetas': recetas})

def receta_detail(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, 'Recetario/receta_detail.html', {'receta': receta})

def receta_create(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        ingredientes = request.POST['ingredientes']
        descripcion = request.POST['descripcion']
        instrucciones = request.POST['instrucciones']
        autor_id = request.POST['autor_id']
        receta = Receta(titulo=titulo, ingredientes=ingredientes, descripcion=descripcion, instrucciones=instrucciones, autor_id=autor_id)
        receta.save()
        #imprimir por consola el objeto
        print(request.POST)
        return redirect('recetas')
    else:
        return render(request, 'Recetario/crear_receta.html')