# 3. Formularios con Bootstrap 5

Para nuestro CRUD, necesitamos un formulario validado. Usaremos `ModelForm` y agregaremos las clases de Bootstrap 5 directamente desde Python para que se rendericen visualmente y se adapten a nuestro diseño.

## Paso 1: Crear `forms.py`
En la carpeta de tu aplicación `pacientes`, crea un nuevo archivo llamado `forms.py`. 
**(Ruta: `pacientes/forms.py`)**

Escribe el siguiente código:

```python
from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'nombre_dueño', 'telefono_contacto']
        
        # Agregamos los widgets para incluir las clases CSS de Bootstrap 5
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la mascota'}),
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'raza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Poodle, Siamés (Opcional)'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_dueño': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo del dueño'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
        }
```
> **Nota**: Con esto aseguramos que cada campo generado por Django tenga la clase `form-control` (o `form-select` para listas desplegables), lo cual hará que tome el estilo atractivo de Bootstrap 5.
