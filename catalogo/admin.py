from django.contrib import admin

from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'precio', 'stock')
    list_filter = ('categoria',)
    search_fields = ('codigo', 'nombre')

