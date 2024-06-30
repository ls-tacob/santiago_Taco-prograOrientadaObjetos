# Programa: Gestor de Contactos
# Este programa permite añadir, mostrar y eliminar contactos
# utilizando una clase para gestionar la información.

class Contacto:
    def __init__(self, nombre, telefono, saldo, activo):
        """
        Inicializa un nuevo contacto.

        Args:
            nombre (str): Nombre del contacto.
            telefono (int): Teléfono del contacto.
            saldo (float): Saldo asociado al contacto.
            activo (bool): Estado de actividad del contacto.
        """
        self.nombre = nombre
        self.telefono = telefono
        self.saldo = saldo
        self.activo = activo

    def mostrar_informacion(self):
        """
        Devuelve la información del contacto en formato legible.
        """
        estado = "Activo" if self.activo else "Inactivo"
        return (f"{self.nombre} - Tel: {self.telefono}, "
                f"Saldo: {self.saldo}, Estado: {estado}")


class GestorContactos:
    def __init__(self):
        """Inicializa la lista de contactos."""
        self.contactos = []

    def agregar_contacto(self, contacto):
        """Añade un contacto a la lista."""
        self.contactos.append(contacto)
        print(f"Contacto {contacto.nombre} añadido con éxito.")

    def mostrar_contactos(self):
        """Muestra todos los contactos almacenados."""
        if not self.contactos:
            print("No hay contactos para mostrar.")
        else:
            for idx, contacto in enumerate(self.contactos, start=1):
                print(f"{idx}. {contacto.mostrar_informacion()}")

    def eliminar_contacto(self, nombre):
        """Elimina un contacto por su nombre."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f"Contacto {nombre} eliminado.")
                return
        print(f"Contacto {nombre} no encontrado.")


def main():
    """Función principal que maneja el menú del gestor de contactos."""
    gestor = GestorContactos()

    while True:
        print("\nGestor de Contactos")
        print("1. Añadir Contacto")
        print("2. Mostrar Contactos")
        print("3. Eliminar Contacto")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = int(input("Teléfono: "))
            saldo = float(input("Saldo: "))
            activo = input("¿Está activo? (sí/no): ").strip().lower() == 'sí'
            nuevo_contacto = Contacto(nombre, telefono, saldo, activo)
            gestor.agregar_contacto(nuevo_contacto)
        elif opcion == "2":
            gestor.mostrar_contactos()
        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            gestor.eliminar_contacto(nombre)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
