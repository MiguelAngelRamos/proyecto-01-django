from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Usuario')
    password = models.CharField(max_length=100, verbose_name='Contraseña')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    

class Movimiento(models.Model):
    # Postgresql no genera un ENUM pero si valida a nivel ORM
    TIPOS = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPOS, verbose_name='Tipo de Movimiento')

    producto = models.ForeignKey('catalogo.Producto', on_delete=models.PROTECT, related_name='movimientos', verbose_name='Producto')
    # related_name permite acceder a los movimientos de un producto desde el producto mismo
    # producto.movimientos.all() -> QuerySet de movimientos relacionados a ese producto

    # PositiveIntegerField -> PostgreSQL -> INTEGER CHECK (cantidad > 0) (rechaza valores negativos o cero)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')

    # auto_now_add -> Postgresql -> timestamp con valor por defecto CURRENT_TIMESTAMP (fecha y hora actual) registra la fecha automaticamente
    fecha = models.DateField(auto_now_add=True, verbose_name='Fecha')

   
    responsable = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='movimientos_realizados', verbose_name='Responsable')

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        ordering = ['-fecha', '-id']  # Ordenar por fecha descendente (más reciente primero)
    
    def __str__(self):
        return f'{self.tipo} - {self.producto.nombre} ({self.cantidad})'