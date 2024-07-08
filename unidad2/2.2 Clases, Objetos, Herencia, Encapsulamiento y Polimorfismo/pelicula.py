from video import Video

class Pelicula(Video):
    def __init__(self, titulo, duracion, director):
        super().__init__(titulo, duracion)
        self._director = director  # Encapsulación: atributo protegido

    def obtener_informacion(self):
        info = super().obtener_informacion()
        return f"{info}, Director: {self._director}"
