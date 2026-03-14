from django.shortcuts import render
from datetime import datetime

## Simula la informacion que obtenemos de una base de datos
PRODUCTOS_DB = [
        {'codigo': 'ARR-001', 'nombre': 'Arroz Grado 1', 'precio': 1200.50, 'stock': 15, 'categoria': 'Abarrotes'},
        {'codigo': 'ACE-002', 'nombre': 'Aceite de Oliva', 'precio': 5500.00, 'stock':0, 'categoria': 'Abarrotes'},
        {'codigo': 'DET-003', 'nombre': 'Detergente Líquido', 'precio': 3000.75, 'stock': 8, 'categoria': 'Limpieza'},
]

def lista_productos(request):
    error = None
    if request.method == 'POST':
        codigo = request.POST.get('codigo').strip().upper();
        codigo_duplicado = False
        for producto in PRODUCTOS_DB:
            if producto['codigo'] == codigo:
                codigo_duplicado = True
                break # No hace seguir revisando si ya encontramos un código duplicado
        if codigo_duplicado:
            error = f'El código "{codigo}" ya existe. Por favor, ingresa un código único.'
        else:
            nuevo_producto = {
                'codigo': codigo,
                'nombre': request.POST.get('nombre'),
                'precio': float(request.POST.get('precio')),
                'stock': int(request.POST.get('stock')),
                'categoria': request.POST.get('categoria'),
            }
            PRODUCTOS_DB.append(nuevo_producto)

    contexto = {
        'fecha_hoy': datetime.now(),
        'productos': PRODUCTOS_DB,
        'tienda': 'Minimarket "Sofia"',
        'error': error
    }    
    return render(request, 'catalogo/lista.html', contexto)

#    if producto['codigo'] == codigo: