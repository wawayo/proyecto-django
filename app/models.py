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