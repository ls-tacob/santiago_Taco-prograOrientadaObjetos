# Programa de Inventario de Productos
"""
Este programa demuestra el uso de clases en Python para gestionar un inventario de productos.
acciones:
- Creación de productos como instancias de la clase Producto.
- Acceso y visualización de los detalles de cada producto.
- Eliminación de productos, lo que activa el destructor para liberar los recursos asociados.

Constructor de la clase Producto.
Inicializa los atributos nombre, precio y cantidad.

:param nombre: Nombre del producto.
:param precio: Precio del producto.
:param cantidad: Cantidad en stock del producto.
"""
class Producto:
    def __init__(self, nombre, precio, cantidad):

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"Producto '{self.nombre}' creado con {self.cantidad} unidades en stock.")

    def __del__(self):
        """
        Destructor de la clase Producto.
        Simula la eliminación del producto del inventario.
        """
        print(f"Producto '{self.nombre}' eliminado del inventario.")

    def mostrar_detalles(self):
        """
        Muestra los detalles del producto.
        """
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")


# Ejemplo de uso del sistema de inventario de productos

# Creación de instancias de Producto
producto1 = Producto("Manzanas", 0.5, 100)
producto2 = Producto("Naranjas", 0.7, 150)

# Acceso a los atributos y métodos del producto
producto1.mostrar_detalles()
producto2.mostrar_detalles()

# Eliminación de instancias de Producto
del producto1
del producto2
