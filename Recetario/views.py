from django.shortcuts import render

# Create your views here.

def welcome_view(request):
    return render(request, 'Recetario/welcome.html')

def recetas_view(request):
    return render(request, 'Recetario/recetas.html')