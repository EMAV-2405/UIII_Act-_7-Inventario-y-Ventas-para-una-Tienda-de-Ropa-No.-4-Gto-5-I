from django.db import models

# -----------------------------
#       CATEGORIA
# -----------------------------
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion_categoria = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    es_activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_categoria


# -----------------------------
#       MARCA
# -----------------------------
class Marca(models.Model):
    nombre_marca = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=50)
    sitio_web = models.CharField(max_length=255, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=20)
    fecha_registro = models.DateField()

    def __str__(self):
        return self.nombre_marca


# -----------------------------
#       PRODUCTO
# -----------------------------
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=50)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto


# -----------------------------
#       CLIENTE
# -----------------------------
class Cliente_Ropa(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    puntos_fidelidad = models.IntegerField(default=0)
    preferencias_estilo = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# -----------------------------
#       EMPLEADO
# -----------------------------
class Empleado_Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# -----------------------------
#       VENTA
# -----------------------------
class Venta_Ropa(models.Model):
    fecha_venta = models.DateTimeField()
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    descuento_total = models.DecimalField(max_digits=5, decimal_places=2)
    estado_venta = models.CharField(max_length=50)

    cliente = models.ForeignKey(Cliente_Ropa, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado_Tienda, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta.date()}"


# -----------------------------
#       DETALLE VENTA
# -----------------------------
class Detalle_Venta_Ropa(models.Model):
    venta = models.ForeignKey(Venta_Ropa, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva_aplicado = models.DecimalField(max_digits=5, decimal_places=2)
    id_talla_vendida = models.CharField(max_length=10)

    def __str__(self):
        return f"Detalle Venta #{self.id} - Producto {self.producto.nombre_producto}"
