# 1. Configuración Inicial del Proyecto (Clínica Veterinaria)

En este caso, crearemos un sistema para una **Clínica Veterinaria**, el cual permitirá gestionar a los pacientes (Mascotas). 
La base de datos sugerida se llamará `vet_clinic_db`.

## Paso 1: Crear el entorno virtual e instalar Django
Abre tu terminal, ubícate en la carpeta donde deseas crear tu proyecto y ejecuta:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Instalar Django
pip install django
```

## Paso 2: Crear el proyecto y la aplicación
```bash
# Crear el proyecto
django-admin startproject clinica_veterinaria .

# Crear la aplicación para gestionar mascotas
python manage.py startapp pacientes
```

## Paso 3: Configurar `settings.py`
Abre el archivo `clinica_veterinaria/settings.py` y realiza los siguientes cambios:

1. **Registrar la aplicación**:
Busca `INSTALLED_APPS` y agrega `'pacientes'`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pacientes', # Nuestra nueva app
]
```

2. **Configurar la base de datos** (Si usas PostgreSQL/MySQL):
Modifica `DATABASES` con el nombre que hemos inventado (`vet_clinic_db`). *Si prefieres seguir usando SQLite por ahora, puedes omitir este paso.*
```python
DATABASES = {
    'default': {
        # Ejemplo con PostgreSQL. Asegúrate de tener instalado psycopg2 (pip install psycopg2)
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vet_clinic_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. **Configurar plantillas (Templates)**:
Asegúrate de configurar la carpeta base para tus templates. Agrega `os` al inicio del archivo y modifica `TEMPLATES`:
```python
import os
# ...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Agregar esta línea
        'APP_DIRS': True,
        # ...
    },
]
```
