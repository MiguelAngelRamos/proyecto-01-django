from django.shortcuts import render, redirect
from datetime import datetime
from .models import Producto, Categoria
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
        if Producto.objects.filter(codigo=codigo).exists():
            error = f'El código "{codigo}" ya existe. Usa un código diferente.'
        else:
            categoria_objeto = Categoria.objects.get(id=request.POST.get('categoria_id'))

            Producto.objects.create(
                codigo=codigo,
                nombre=request.POST.get('nombre', '').strip(),
                precio=float(request.POST.get('precio', 0)),
                stock=int(request.POST.get('stock',0)),
                categoria=categoria_objeto
            )
            return redirect('lista_productos')
        #* codigo antiguo artesanal


    contexto = {
        'fecha_hoy': datetime.now(),
        'productos': PRODUCTOS_DB,
        'tienda': 'Minimarket "Sofia"',
        'error': error
    }    
    return render(request, 'catalogo/lista.html', contexto)

#    if producto['codigo'] == codigo: