from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.views.decorators.csrf import csrf_exempt # Desactivo el csrf porque no me deja hacer peticiones POST desde el formulario

from app.models import Agenda, Nota, Tarea
# Create your views here.

def index(request):
  template = loader.get_template('index.html')
  render = template.render({'agendas': Agenda.objects.all()})
  return HttpResponse(render)

@csrf_exempt
def apuntes(request, id):
  try:
    agenda = Agenda.objects.get(id=id)
    notas = Nota.objects.filter(agenda=agenda)
    tareas = Tarea.objects.filter(agenda=agenda)

    if request.method == 'POST':
      titulo = request.POST['titulo']
      descripcion = request.POST['descripcion']
      tipo = request.POST['tipo']

      if tipo == 'nota':
        nota = Nota(titulo=titulo, descripcion=descripcion, agenda=agenda)
        nota.save()
      else:
        tarea = Tarea(titulo=titulo, descripcion=descripcion, agenda=agenda)
        tarea.save()

      template = loader.get_template('apuntes.html')
      context = {'agenda': agenda, 'notas': notas, 'tareas': tareas}
      render = template.render(context)
      return HttpResponse(render)

  except Agenda.DoesNotExist:
    return redirect('index')

  template = loader.get_template('apuntes.html')
  context = {'agenda': agenda, 'notas': notas, 'tareas': tareas}
  render = template.render(context)
  return HttpResponse(render)



@csrf_exempt
def crear_agenda(request):
  if request.method == 'POST':
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    agenda = Agenda(nombre=nombre, descripcion=descripcion)
    
    #si el nombre de la agenda ya existe, no se crea
    if len(Agenda.objects.filter(nombre=nombre)) > 0:
      template = loader.get_template('index.html')
      render = template.render({'agendas': Agenda.objects.all()})
      return HttpResponse(render)
      
    else:
      agenda.save()
    
    template = loader.get_template('index.html')
    render = template.render({'agendas': Agenda.objects.all(), 'mensaje': 'Agenda creada correctamente'})
    return HttpResponse(render)

  else:
    template = loader.get_template('index.html')
    render = template.render({'agendas': Agenda.objects.all()})
    return HttpResponse(render)

