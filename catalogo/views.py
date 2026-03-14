from django.shortcuts import render
from datetime import datetime

## Simula la informacion que obtenemos de una base de datos
PRODUCTOS_DB = [
        {'nombre': 'Arroz Grado 1', 'precio': 1200.50, 'stock': 15, 'categoria': 'Abarrotes'},
        {'nombre': 'Aceite de Oliva', 'precio': 5500.00, 'stock':0, 'categoria': 'Abarrotes'},
        {'nombre': 'Detergente Líquido', 'precio': 3000.75, 'stock': 8, 'categoria': 'Limpieza'},
]

def lista_productos(request):
    if request.method == 'POST':
        nuevo_producto = {
            'nombre': request.POST.get('nombre'),
            'precio': float(request.POST.get('precio')),
            'stock': int(request.POST.get('stock')),
            'categoria': request.POST.get('categoria'),
        }
        PRODUCTOS_DB.append(nuevo_producto)

    contexto = {
        'fecha_hoy': datetime.now(),
        'productos': PRODUCTOS_DB,
        'tienda': 'Minimarket "Sofia"'
    }    
    return render(request, 'catalogo/lista.html', contexto)