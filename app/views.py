from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.views.decorators.csrf import csrf_exempt # Desactivo el csrf porque no me deja hacer peticiones POST desde el formulario

from app.models import Agenda
# Create your views here.

def index(request):
  template = loader.get_template('index.html')
  render = template.render()
  return HttpResponse(render)

def apuntes(request):
  template = loader.get_template('apuntes.html')
  render = template.render()
  return HttpResponse(render)

@csrf_exempt
def crear_agenda(request):
  if request.method == 'POST':
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    agenda = Agenda(nombre=nombre, descripcion=descripcion)
    agenda.save()
    return HttpResponse('Agenda creada')
  else:
    return HttpResponse('No se ha podido crear la agenda')

