from django.shortcuts import render, redirect
from datetime import datetime
from .models import Producto, Categoria

def lista_productos(request):
    error = None
    if request.method == 'POST':
        codigo = request.POST.get('codigo').strip().upper();
        if Producto.objects.filter(codigo=codigo).exists():
            error = f'El código "{codigo}" ya existe. Usa un código diferente.'
        else:
            categoria_objeto = Categoria.objects.get(id=request.POST.get('categoria_id'))
            #* SELECT * FROM catalogo_categoria WHERE id = 1

            #* Detras de escena se genera el sql
            #* INSERT INTO catalogo_producto (codigo, nombre, precio, stock, categoria_id) VALUES (codigo, nombre, precio, stock, categoria_id)
            Producto.objects.create(
                codigo=codigo,
                nombre=request.POST.get('nombre', '').strip(),
                precio=float(request.POST.get('precio', 0)),
                stock=int(request.POST.get('stock',0)),
                categoria=categoria_objeto
            )
            return redirect('lista_productos')

    contexto = {
        'fecha_hoy': datetime.now(),
        'productos': Producto.objects.select_related('categoria').all(),
        'categorias': Categoria.objects.all(),
        'tienda': 'Minimarket "Sofia"',
        'error': error
    }    
    return render(request, 'catalogo/lista.html', contexto)

#    if producto['codigo'] == codigo: