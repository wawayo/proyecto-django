from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Recetario.views import *


urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('recetas/', recetas_view, name='recetas'),
    path('recetas/crear/', receta_create, name='crear-receta'),
    path('recetas/<int:id>/', receta_detail, name='detalle-receta'),
    path('admin/', admin.site.urls),
]  
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# Para poder servir archivos estáticos en desarrollo
