class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa los atributos del producto: ID, nombre, cantidad y precio.
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def mostrar_info(self):
        # Retorna una cadena con la información del producto en un formato legible.
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    @staticmethod
    def from_string(data):
        # Crea un objeto Producto a partir de una cadena de texto.
        id_producto, nombre, cantidad, precio = data.split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))

    def to_string(self):
        # Convierte un objeto Producto en una cadena de texto para almacenar en archivo.
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        # Inicializa el inventario con un diccionario vacío y carga los productos desde un archivo.
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        # Carga los productos desde el archivo de inventario al diccionario.
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    producto = Producto.from_string(linea.strip())
                    self.productos[producto.id_producto] = producto
        except FileNotFoundError:
            # Si el archivo no existe, lo notifica y espera para crear uno nuevo cuando se agregue un producto.
            print(f"Archivo {self.archivo} no encontrado. Se creará un nuevo archivo al agregar productos.")
        except PermissionError:
            # Maneja errores de permiso al intentar leer el archivo.
            print(f"Error: No tienes permiso para leer el archivo {self.archivo}.")

    def guardar_inventario(self):
        # Guarda todos los productos en el archivo de inventario.
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(producto.to_string() + '\n')
        except PermissionError:
            # Maneja errores de permiso al intentar escribir en el archivo.
            print(f"Error: No tienes permiso para escribir en el archivo {self.archivo}.")

    def agregar_producto(self, producto):
        # Agrega un producto al inventario y lo guarda en el archivo.
        if producto.id_producto in self.productos:
            print("Error: ID de producto ya existente.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()  # Guarda los cambios en el archivo.
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario y actualiza el archivo.
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()  # Guarda los cambios en el archivo.
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # Actualiza la cantidad y/o el precio de un producto y guarda los cambios en el archivo.
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            self.guardar_inventario()  # Guarda los cambios en el archivo.
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca productos por nombre (o parte del nombre) y los muestra.
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p.mostrar_info())
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_productos(self):
        # Muestra todos los productos en el inventario.
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto.mostrar_info())


def menu():
    # Interfaz de usuario en la consola para interactuar con el inventario.
    inventario = Inventario()
    while True:
        # Muestra el menú de opciones al usuario.
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            # Opción para salir del programa.
            print("Saliendo del sistema.")
            break
        elif opcion == '1':
            # Opción para agregar un nuevo producto.
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo_producto)
        elif opcion == '2':
            # Opción para eliminar un producto existente.
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Opción para actualizar la cantidad o el precio de un producto.
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
        elif opcion == '4':
            # Opción para buscar un producto por nombre.
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Opción para mostrar todos los productos en el inventario.
            inventario.mostrar_todos_productos()
        else:
            # Mensaje de error si se ingresa una opción no válida.
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    # Llama a la función de menú para iniciar el programa.
    menu()
