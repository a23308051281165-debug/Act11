from django.db import models

class Producto(models.Model):
    ID_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    unidad_medida = models.CharField(max_length=20, help_text="Ejemplo: kg, g, pieza, litro")
    fotografia = models.ImageField(upload_to='img_productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='proveedores')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
