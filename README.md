# Proyecto Django

Este repositorio contiene un proyecto desarrollado en Django, un framework de desarrollo web en Python. A continuación, se detallan los pasos necesarios para clonar el repositorio, configurar el entorno virtual, instalar las dependencias, aplicar migraciones, iniciar el servidor de desarrollo y crear un superusuario.

## Clonar el repositorio desde GitHub:
```shell
git clone https://github.com/Leo-Spj/proyecto-django.git
```

## Crear un entorno virtual:
```shell
python -m venv venv
```

## Activar el entorno virtual

en sistemas Unix:

```shell
source venv/bin/activate
```

en Windows:

```shell
venv\Scripts\activate
```

## Instalar las dependencias:
```shell
pip install -r requirements.txt
```

## Aplicar migraciones:
```shell
python manage.py migrate
```

## Crear un superusuario:
```shell
python manage.py createsuperuser
```

## Iniciar el servidor de desarrollo:
```shell
python manage.py runserver
```