from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

def crear_agenda(request):
  print(request.POST)

