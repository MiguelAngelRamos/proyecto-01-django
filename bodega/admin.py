from django.contrib import admin
from .models import Usuario, Movimiento

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'producto', 'cantidad', 'fecha', 'responsable')
    list_filter = ('tipo', 'fecha')
    search_fields = ('responsable', 'producto__nombre')