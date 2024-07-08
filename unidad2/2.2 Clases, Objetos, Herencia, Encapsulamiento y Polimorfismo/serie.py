from video import Video

class Serie(Video):
    def __init__(self, titulo, duracion, temporada, episodio):
        super().__init__(titulo, duracion)
        self._temporada = temporada  # Encapsulación: atributo protegido
        self._episodio = episodio  # Encapsulación: atributo protegido

    def obtener_informacion(self):
        info = super().obtener_informacion()
        return f"{info}, Temporada: {self._temporada}, Episodio: {self._episodio}"
