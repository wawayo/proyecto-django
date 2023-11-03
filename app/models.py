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

# from app.models import Agenda, Nota, Tarea

# limpia la base de datos:
# Agenda.objects.all().delete()
# Nota.objects.all().delete()
# Tarea.objects.all().delete()

# crea una agenda:
# agenda1 = Agenda(nombre='Python', descripcion='Apuntes de Python')
# agenda1.save()
# agenda2 = Agenda(nombre='Django', descripcion='Apuntes de Django')
# agenda2.save()

# crea una nota:
# nota1 = Nota(titulo='Variables', descripcion='Variables en Python', agenda=agenda1)
# nota1.save()
# nota2 = Nota(titulo='Funciones', descripcion='Funciones en Python', agenda=agenda1)
# nota2.save()
# nota3 = Nota(titulo='Variables', descripcion='Variables en Django', agenda=agenda2)
# nota3.save()
# nota4 = Nota(titulo='Funciones', descripcion='Funciones en Django', agenda=agenda2)
# nota4.save()

# crea una tarea:
# tarea1 = Tarea(titulo='Variables', descripcion='Variables en Python', agenda=agenda1)
# tarea1.save()
# tarea2 = Tarea(titulo='Funciones', descripcion='Funciones en Python', agenda=agenda1)
# tarea2.save()
# tarea3 = Tarea(titulo='Variables', descripcion='Variables en Django', agenda=agenda2)
# tarea3.save()
# tarea4 = Tarea(titulo='Funciones', descripcion='Funciones en Django', agenda=agenda2)
# tarea4.save()

