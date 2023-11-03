from django.db import models

# Create your models here.

class Agenda(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Nota(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=False)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    

# mediantes python manage.py shell:
'''
from app.models import Agenda, Nota, Tarea

Agenda.objects.all().delete()
Nota.objects.all().delete()
Tarea.objects.all().delete()


agenda1 = Agenda(nombre='Python', descripcion='Apuntes de Python')
agenda1.save()
agenda2 = Agenda(nombre='Django', descripcion='Apuntes de Django')
agenda2.save()

nota1 = Nota(titulo='Arrays', descripcion='Los principales métodos de los arrays son push, pop.', agenda=agenda1)
nota1.save()
nota2 = Nota(titulo='Funciones', descripcion='Las funciones son bloques de código que se pueden reutilizar.', agenda=agenda1)
nota2.save()
nota3 = Nota(titulo='Templates en Django', descripcion='Los templates en Django son archivos HTML que se pueden reutilizar. Se pueden definir variables con {{ variable }}.', agenda=agenda2)
nota3.save()
nota4 = Nota(titulo='Modelos en Django', descripcion='Los modelos en Django son clases que representan tablas de la base de datos. Se pueden definir con la clase Model.', agenda=agenda2)
nota4.save()

tarea1 = Tarea(titulo='Primer avance Python', descripcion='Emplear el uso correcto de variables', agenda=agenda1)
tarea1.save()
tarea2 = Tarea(titulo='Segundo avance Python', descripcion='Uso correcto de funciones', agenda=agenda1)
tarea2.save()
tarea3 = Tarea(titulo='Primer avance Django', descripcion='Emplear el uso correcto de templates', agenda=agenda2)
tarea3.save()
tarea4 = Tarea(titulo='Segundo avance Django', descripcion='Uso correcto de modelos', agenda=agenda2)
tarea4.save()

'''