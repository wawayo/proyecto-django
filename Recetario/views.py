from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.

def welcome_view(request):
    return render(request, 'Recetario/welcome.html')

def recetas_view(request):
    recetas = Receta.objects.all()
    return render(request, 'Recetario/recetas.html', {'recetas': recetas})

def perfil_view(request):
    recetas = Receta.objects.filter(autor_id=request.user.id)
    return render(request, 'Recetario/perfil.html', {'recetas': recetas})

def detalle_receta(request, id):
    try:
        receta = Receta.objects.get(id=id)
        comentarios = Comentario.objects.filter(receta_id=id)
        return render(request, 'Recetario/detalle_receta.html', {'receta': receta, 'comentarios': comentarios})
    except Receta.DoesNotExist:
        return render(request, 'Recetario/recetas.html', {'mensaje': 'La receta no existe'})

@login_required(login_url='/admin/')
def receta_create(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        ingredientes = request.POST['ingredientes']
        descripcion = request.POST['descripcion']
        instrucciones = request.POST['instrucciones']
        autor_id = request.POST['autor_id']
        receta = Receta(titulo=titulo, ingredientes=ingredientes, descripcion=descripcion, instrucciones=instrucciones, autor_id=autor_id)
        receta.save()

        return redirect('recetas')
    else:
        return render(request, 'Recetario/crear_receta.html')

@login_required(login_url='/admin/')   
def comentario_create(request):
    if request.method == 'POST':
        autor_id = request.POST['autor_id']
        receta_id = request.POST['receta_id']
        texto = request.POST['texto']
        comentario = Comentario(autor_id=autor_id, receta_id=receta_id, texto=texto)
        comentario.save()
        return redirect('detalle-receta', id=receta_id)
    else:
        return redirect('recetas')
    
def buscar_receta(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        nombre = Receta.objects.filter(titulo__contains=titulo)
        ingredientes = Receta.objects.filter(ingredientes__contains=titulo)
        descripcion = Receta.objects.filter(descripcion__contains=titulo)
        recetas = nombre.union(ingredientes, descripcion)

        if recetas.count() == 0:
            return render(request, 'Recetario/recetas.html', {'recetas': recetas, 'mensaje': 'No se encontraron resultados'})
        
        return render(request, 'Recetario/recetas.html', {'recetas': recetas})

    else:
        return redirect('recetas')