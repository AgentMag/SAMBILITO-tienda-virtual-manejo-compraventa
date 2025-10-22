from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Definir una tupla con los valores del select genero_empleado
generos = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro"),
)

#modelo de las categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#modelo de los productos
class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=200)# nombre del producto
    apellido_empleado = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    edad_empleado = models.PositiveIntegerField(default=0)#stok para los productos
    contador_producto= models.PositiveIntegerField(default=0)
    salario_empleado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    foto_empleado = models.ImageField(upload_to='fotos_empleados/', null=True, blank=True)
    activo = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def es_extension_valida(self):
        extensiones_validas = ['.jpg', '.jpeg', '.png', '.gif']
        return any(self.foto_empleado.name.lower().endswith(ext) for ext in extensiones_validas)

    """ la clase Meta dentro de un modelo se utiliza para proporcionar metadatos adicionales sobre el modelo."""
    class Meta:
        db_table = "empleados"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre_empleado} {self.apellido_empleado}"



#el carrito de compras
class Producto(models.Model):
    nombre_empleado = models.CharField(max_length=200)# nombre del producto
    apellido_empleado = models.CharField(max_length=100)
    precio = models.IntegerField()
    stok = models.PositiveIntegerField(default=0)#cantidad de productos

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    


    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    

# Historial de búsqueda

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.query}"
    

#model para los pedidos
class Pedido(models.Model):
    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('pago movil', 'Pago Móvil'),
        ('transferencia', 'Transferencia'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    codigo = models.CharField(max_length=100)
    monto_usd = models.DecimalField(max_digits=10, decimal_places=2)
    monto_bs = models.DecimalField(max_digits=12, decimal_places=2)
    tasa = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=METODOS_PAGO, default='efectivo')
    metodo_entrega = models.CharField(max_length=100, default="Retiro en tienda")

    def __str__(self):
        return f"Pedido {self.codigo} - {self.usuario}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto} x{self.cantidad}"
