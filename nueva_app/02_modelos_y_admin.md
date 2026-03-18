# 2. Creación de Modelos y Admin

Vamos a crear el modelo `Mascota` para registrar a nuestros pacientes, y lo agregaremos al panel de administración de Django.

## Paso 1: Crear el Modelo `Mascota`
Abre el archivo `pacientes/models.py` y escribe el siguiente código:

```python
from django.db import models

class Mascota(models.Model):
    ESPECIES = [
        ('PERRO', 'Perro'),
        ('GATO', 'Gato'),
        ('AVE', 'Ave'),
        ('OTRO', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIES)
    raza = models.CharField(max_length=100, blank=True, null=True)
    edad = models.PositiveIntegerField(help_text="Edad en años")
    nombre_dueño = models.CharField(max_length=150)
    telefono_contacto = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_especie_display()}) - Dueño: {self.nombre_dueño}"
```

## Paso 2: Ejecutar Migraciones
Ahora que tenemos el modelo creado (y configuraste la base de datos `vet_clinic_db` si no usas sqlite3), debes aplicar las migraciones. En la terminal ejecuta:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Paso 3: Registrar el Modelo en el Panel de Administración
Para poder gestionar las mascotas desde el sitio de administrador, abre `pacientes/admin.py`:

```python
from django.contrib import admin
from .models import Mascota

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'nombre_dueño', 'telefono_contacto', 'fecha_registro')
    search_fields = ('nombre', 'nombre_dueño')
    list_filter = ('especie',)
```

Puedes crear un superusuario para probar el panel de admin (opcional):
```bash
python manage.py createsuperuser
```
