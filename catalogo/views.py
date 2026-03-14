from django.shortcuts import render
from datetime import datetime

def lista_productos(request):
    if request.method == 'POST':
        print("Formulario recibido:", request.POST)
    ## Simula la informacion que obtenemos de una base de datos
    productos = [
        {'nombre': 'Arroz Grado 1', 'precio': 1200.50, 'stock': 15, 'categoria': 'Abarrotes'},
        {'nombre': 'Aceite de Oliva', 'precio': 5500.00, 'stock':0, 'categoria': 'Abarrotes'},
        {'nombre': 'Detergente Líquido', 'precio': 3000.75, 'stock': 8, 'categoria': 'Limpieza'},
    ]

    contexto = {
        'fecha_hoy': datetime.now(),
        'productos': productos,
        'tienda': 'Minimarket "Sofia"'
    }    
    return render(request, 'catalogo/lista.html', contexto)