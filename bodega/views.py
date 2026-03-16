from django.shortcuts import render

# Create your views here.
USUARIOS_DB = {
    'admin': '1234',
    'sofia': 'academy',
}

MOVIMIENTOS_DB = [
    {'tipo': 'Entrada', 'producto': 'Arroz Grado 1',      'cantidad': 50, 'fecha': '10/03/2026', 'responsable': 'admin'},
    {'tipo': 'Salida',  'producto': 'Aceite de Oliva',    'cantidad':  3, 'fecha': '11/03/2026', 'responsable': 'sofia'},
    {'tipo': 'Entrada', 'producto': 'Detergente Líquido', 'cantidad': 20, 'fecha': '12/03/2026', 'responsable': 'admin'},
]

def login_view(request):
    pass

def logout_view(request):
    pass

def panel_view(request):
    pass