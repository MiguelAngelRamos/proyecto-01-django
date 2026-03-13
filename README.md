## Crear proyecto 

```sh
mkdir minimarket_project
cd minimarket_project
```

Con tu terminal apuntando a la carpeta ***minimarket_project***


## Crear el entorno virtual 

```sh
python -m venv venv
```

## Activar el entorno virtual 

```sh
.\venv\Scripts\activate
```

## Instalar Django

```sh
pip install django
```


## Creación del Proyecto y la App (DJANGO)

1. Proyecto
```sh
django-admin startproject core .
```

2. la App

```sh
python manage.py startapp catalogo
```

## Configuracion dentro de "core"

En core/settings.py, debemos registrar la app y configurar las rutas de carpetas

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo', # esto es nuestra app
]

```