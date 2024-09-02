# main.py

from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

def menu():

    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Quitar Libro\n3. Registrar Usuario\n4. Dar Baja Usuario\n5. Prestar Libro\n6. Devolver Libro\n7. Buscar Libro\n8. Listar Libros\n9. Listar Libros Prestados\n10. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '10':
            print("Saliendo del sistema.")
            break
        elif opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
        elif opcion == '4':
            id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == '5':
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario que recibe el libro: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        elif opcion == '6':
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario que devuelve el libro: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        elif opcion == '7':
            criterio = input("Ingrese el criterio de búsqueda (titulo, autor, categoria): ")
            valor = input(f"Ingrese el valor a buscar por {criterio}: ")
            libros_encontrados = biblioteca.buscar_libro(criterio, valor)
            for libro in libros_encontrados:
                print(libro)
        elif opcion == '8':
            print("\nLibros disponibles en la biblioteca:")
            for libro in biblioteca.listar_libros():
                print(libro)
        elif opcion == '9':
            id_usuario = input("Ingrese el ID del usuario para listar sus libros prestados: ")
            print(f"\nLibros prestados a {id_usuario}:")
            for libro in biblioteca.listar_libros_prestados(id_usuario):
                print(libro)
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
