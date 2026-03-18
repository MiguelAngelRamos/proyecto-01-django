from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # VARCHAR(20) UNIQUE NOT NULL
    # Chardfiel ya es not null por defecto y si deseas que esto permita valores null, debes agregar null=True
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0, verbose_name='Stock')
    #* FK -> columna "categoria_id" va ser la FOREIGN KEY
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos', verbose_name='Categoría')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    # Este es el metodo to string, es decir, lo que se va a mostrar cuando se imprima un objeto de tipo producto
    def __str__(self):
        return f'{self.codigo} ({self.nombre})'
    """
    lacteos = Categoria.objects.get(nombre='Lácteos')
    lacteos.productos.all() -> QuerySet de productos relacionados a la categoria lacteos
    1 ES EL ID DE LA CATEGORIA LACTEOS
    SELECT * FROM catalogo_producto WHERE categoria_id = 1;
    """