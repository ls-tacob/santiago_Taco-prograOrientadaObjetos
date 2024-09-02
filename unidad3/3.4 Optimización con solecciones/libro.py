# libro.py

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Creamos una tupla para los atributos inmutables del libro.
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        # Representación en formato legible del libro.
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - Categoría: {self.categoria}"

    @staticmethod
    def from_string(data):
        # Crea un objeto Libro a partir de una cadena de texto.
        titulo, autor, categoria, isbn = data.split(',')
        return Libro(titulo, autor, categoria, isbn)

    def to_string(self):
        # Convierte un objeto Libro en una cadena de texto para almacenar en archivo.
        return f"{self.titulo},{self.autor},{self.categoria},{self.isbn}"
