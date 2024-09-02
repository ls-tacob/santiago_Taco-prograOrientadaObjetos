# biblioteca.py

import os
from libro import Libro
from usuario import Usuario

class Biblioteca:
    def __init__(self, archivo_libros='libros.txt', archivo_usuarios='usuarios.txt'):
        # Diccionario para almacenar libros por ISBN.
        self.libros = {}
        # Diccionario para almacenar usuarios por ID.
        self.usuarios = {}
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.cargar_libros()
        self.cargar_usuarios()

    def cargar_libros(self):
        if os.path.exists(self.archivo_libros):
            with open(self.archivo_libros, 'r') as file:
                for linea in file:
                    libro = Libro.from_string(linea.strip())
                    self.libros[libro.isbn] = libro
        else:
            print(f"Archivo {self.archivo_libros} no encontrado. Se creará un nuevo archivo al agregar libros.")

    def guardar_libros(self):
        with open(self.archivo_libros, 'w') as file:
            for libro in self.libros.values():
                file.write(libro.to_string() + '\n')

    def cargar_usuarios(self):
        if os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, 'r') as file:
                for linea in file:
                    nombre, id_usuario = linea.strip().split(',')
                    self.usuarios[id_usuario] = Usuario(nombre, id_usuario)
        else:
            print(f"Archivo {self.archivo_usuarios} no encontrado. Se creará un nuevo archivo al agregar usuarios.")

    def guardar_usuarios(self):
        with open(self.archivo_usuarios, 'w') as file:
            for usuario in self.usuarios.values():
                file.write(f"{usuario.nombre},{usuario.id_usuario}\n")

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("Error: ISBN de libro ya existente.")
        else:
            self.libros[libro.isbn] = libro
            self.guardar_libros()
            print("Libro añadido exitosamente.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_libros()
            print("Libro eliminado exitosamente.")
        else:
            print("Error: Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("Error: ID de usuario ya existente.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.guardar_usuarios()
            print("Usuario registrado exitosamente.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.guardar_usuarios()
            print("Usuario dado de baja exitosamente.")
        else:
            print("Error: Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)
            self.quitar_libro(isbn)
            print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
        else:
            print("Error: ISBN o ID de usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
            if libro:
                usuario.devolver_libro(libro)
                self.añadir_libro(libro)
                print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
            else:
                print("Error: Libro no encontrado entre los prestados.")
        else:
            print("Error: ID de usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        if criterio not in ['titulo', 'autor', 'categoria']:
            raise ValueError("Criterio de búsqueda no válido. Usa 'titulo', 'autor' o 'categoria'.")
        encontrados = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        return encontrados

    def listar_libros(self):
        return self.libros.values()

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.listar_libros_prestados()
        else:
            print("Error: ID de usuario no encontrado.")
            return []
