# usuario.py

class Usuario:
    def __init__(self, nombre, id_usuario):
        # Inicializa los atributos del usuario.
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Usamos una lista para gestionar los libros prestados a cada usuario.
        self.libros_prestados = []

    def prestar_libro(self, libro):
        # Agrega un libro a la lista de libros prestados.
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        # Elimina un libro de la lista de libros prestados.
        self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        # Devuelve la lista de libros prestados.
        return self.libros_prestados

    def __repr__(self):
        return self.nombre
