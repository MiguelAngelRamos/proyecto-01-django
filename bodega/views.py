from django.shortcuts import render, redirect
from datetime import datetime

from catalogo.models import Producto
from .models import Usuario, Movimiento


def login_view(request):
    if 'usuario' in request.session:
        return redirect('panel_bodega')
    error = None
    if request.method == 'POST':
        usuario = request.POST.get('usuario', '').strip()
        password = request.POST.get('password', '').strip()
        #* SELECT * FROM bodega_usuario WHERE nombre = usuario AND password = password LIMIT 1
        usuario_objeto = Usuario.objects.filter(nombre=usuario, password=password).first()
        ## validamos
        if usuario_objeto:
            # Creamos o guardamos la session
            request.session['usuario'] = usuario_objeto.nombre  # Guardamos solo el nombre en la sesión para evitar almacenar información sensible
            return redirect('panel_bodega')
        else:
            error = 'credenciales incorrectas'
    return render(request, 'bodega/login.html', {'error':error})

def logout_view(request):
    request.session.flush()  # Limpiar la sesión por seguridad
    return redirect('login_bodega')

def panel_bodega(request):
    # Debe verificar si el usuario esta autenticado, sino redirigir al login
    usuario_session = request.session.get('usuario')
    #* SELECT * FROM bodega_usuario WHERE nombre = usuario_session LIMIT 1
    usuario_objeto = Usuario.objects.filter(nombre=usuario_session).first()
    if not usuario_session or not usuario_objeto:
        request.session.flush()  # Limpiar la sesión por seguridad
        return redirect('login_bodega')
    
    error = None
    if request.method == 'POST':
        nuevo_movimiento = {
            'tipo': request.POST.get('tipo', ''),
            'producto': request.POST.get('producto', '').strip(),
            'cantidad': int(request.POST.get('cantidad', 0)),
            'fecha': datetime.now().strftime('%d/%m/%Y'),
            'responsable': usuario_session,
        }
        MOVIMIENTOS_DB.append(nuevo_movimiento)
        return redirect('panel_bodega')

    #  SELECT * FROM bodega_movimiento JOIN catalogo_producto ON bodega_movimiento.producto_id = catalogo_producto.id JOIN bodega_usuario ON bodega_movimiento.responsable_id = bodega_usuario.id esto equivale a -> 'movimientos': Movimiento.objects.select_related('producto', 'responsable').all()
    
    contexto = {
            'movimientos': Movimiento.objects.select_related('producto', 'responsable').all(),
            'usuario': usuario_session,
            'total_movimientos': Movimiento.objects.count(),
            'productos': Producto.objects.all(), # SELECT * FROM catalogo_producto
            'error': error
    }
    return render(request, 'bodega/panel.html', contexto)
