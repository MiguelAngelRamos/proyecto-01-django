# 5. Plantillas (Templates) con Bootstrap 5

Es hora de armar el lado visual de la aplicación construyendo las plantillas HTML que llamamos en nuestras vistas. 

Asegúrate de crear una carpeta llamada `templates` **en la raíz del proyecto** (al mismo nivel que `manage.py`) y dentro de ella crear otra carpeta llamada `pacientes`.

Estructura de carpetas a crear:
```text
(raíz del proyecto)/
├── templates/
│   ├── base.html
│   └── pacientes/
│       ├── mascota_list.html
│       ├── mascota_form.html
│       └── mascota_confirm_delete.html
```

## Paso 1: Plantilla Base (`templates/base.html`)
Este archivo cargará el CSS y JS de **Bootstrap 5** a través de CDN, además del navbar o menú de navegación para tu sistema.
Abre o crea `templates/base.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clínica Veterinaria</title>
    <!-- Bootstrap 5 CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
    <div class="container">
        <a class="navbar-brand" href="{% url 'mascota_list' %}">🐾 Clínica Vet</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link text-white" href="{% url 'mascota_create' %}">Registrar Mascota</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div class="container">
    {% block content %}
    <!-- Aquí se inyectará el contenido de las demás plantillas -->
    {% endblock %}
</div>

<!-- Bootstrap 5 JS Bundle CDN -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

## Paso 2: Listado de Mascotas (`templates/pacientes/mascota_list.html`)
Mostrará la tabla con todas las mascotas registradas en la base de datos.
Crea o abre el archivo en la ruta correspondiente:

```html
{% extends 'base.html' %}

{% block content %}
<div class="d-flex justify-content-between align-items-center mb-3">
    <h2>Listado de Pacientes (Mascotas)</h2>
    <a href="{% url 'mascota_create' %}" class="btn btn-success">➕ Nuevo Paciente</a>
</div>

<div class="card shadow-sm">
    <div class="card-body">
        <table class="table table-hover align-middle">
            <thead class="table-dark">
                <tr>
                    <th>Nombre</th>
                    <th>Especie</th>
                    <th>Raza</th>
                    <th>Dueño</th>
                    <th>Teléfono</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                {% for mascota in mascotas %}
                <tr>
                    <td>{{ mascota.nombre }}</td>
                    <td>{{ mascota.get_especie_display }}</td>
                    <td>{{ mascota.raza|default:"N/A" }}</td>
                    <td>{{ mascota.nombre_dueño }}</td>
                    <td>{{ mascota.telefono_contacto }}</td>
                    <td>
                        <a href="{% url 'mascota_update' mascota.pk %}" class="btn btn-sm btn-warning">Editar</a>
                        <a href="{% url 'mascota_delete' mascota.pk %}" class="btn btn-sm btn-danger">Eliminar</a>
                    </td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="6" class="text-center">No hay mascotas registradas aún.</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}
```

## Paso 3: Formulario Crear/Editar (`templates/pacientes/mascota_form.html`)
Esta plantilla se reutiliza para **crear registros** y para **actualizarlos**, gracias a las vistas genéricas.
Abre y pon el siguiente código en la ruta indicada:

```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card shadow-sm">
            <div class="card-header bg-primary text-white">
                <!-- Cambiamos el título si le pasamos una instancia a actualizar -->
                <h4 class="mb-0">{% if object %}Editar Paciente{% else %}Registrar Nuevo Paciente{% endif %}</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    <!-- Renderizamos el formulario que preparamos en forms.py -->
                    {{ form.as_p }}
                    
                    <div class="d-flex justify-content-end mt-4">
                        <a href="{% url 'mascota_list' %}" class="btn btn-secondary me-2">Cancelar</a>
                        <button type="submit" class="btn btn-primary">Guardar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## Paso 4: Confirmación de Eliminación (`templates/pacientes/mascota_confirm_delete.html`)
Muestra una advertencia antes de eliminar físicamente un registro.

```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card shadow-sm border-danger">
            <div class="card-body text-center">
                <h3 class="text-danger mb-4">¿Estás seguro?</h3>
                <p>¿Realmente deseas eliminar el registro de la mascota <strong>{{ object.nombre }}</strong>?</p>
                <p class="text-muted"><small>Esta acción no se puede deshacer.</small></p>
                
                <form method="post" class="mt-4">
                    {% csrf_token %}
                    <a href="{% url 'mascota_list' %}" class="btn btn-secondary me-2">Cancelar</a>
                    <button type="submit" class="btn btn-danger">Sí, eliminar</button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---
**¡Felicidades!** Una vez hayas completado todos los pasos de los 5 archivos, podrás iniciar tu servidor con `python manage.py runserver` y probar tu CRUD completamente funcional basado en una Clínica Veterinaria, estilizado con Bootstrap 5.
