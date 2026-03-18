# 4. Vistas y URLs (CRUD Lógico)

Vamos a utilizar las Vistas Basadas en Clases (Class-Based Views) de Django, ya que son más rápidas, limpias de implementar, y perfectas para un CRUD.

## Paso 1: Crear las Vistas (`pacientes/views.py`)
Abre el archivo `pacientes/views.py` y reemplaza todo su contenido por lo siguiente:

```python
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Mascota
from .forms import MascotaForm

# R: READ (List) - Mostrar todos los registros
class MascotaListView(ListView):
    model = Mascota
    template_name = 'pacientes/mascota_list.html'
    context_object_name = 'mascotas'

# C: CREATE - Crear nuevo registro
class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'pacientes/mascota_form.html'
    success_url = reverse_lazy('mascota_list')

# U: UPDATE - Actualizar un registro existente
class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'pacientes/mascota_form.html'
    success_url = reverse_lazy('mascota_list')

# D: DELETE - Eliminar registro
class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'pacientes/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascota_list')
```

## Paso 2: Crear las URLs de la aplicación (`pacientes/urls.py`)
Crea un archivo nuevo llamado `urls.py` dentro de la carpeta `pacientes`. **(Ruta: `pacientes/urls.py`)**:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MascotaListView.as_view(), name='mascota_list'),
    path('nueva/', views.MascotaCreateView.as_view(), name='mascota_create'),
    path('editar/<int:pk>/', views.MascotaUpdateView.as_view(), name='mascota_update'),
    path('eliminar/<int:pk>/', views.MascotaDeleteView.as_view(), name='mascota_delete'),
]
```

## Paso 3: Conectar las URLs en el proyecto principal
Abre el archivo principal `clinica_veterinaria/urls.py` (dentro de tu proyecto) y agrega la función `include` para enlazar nuestras nuevas URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Conectamos las URLs de la app pacientes en la ruta raíz del proyecto
    path('', include('pacientes.urls')), 
]
```
