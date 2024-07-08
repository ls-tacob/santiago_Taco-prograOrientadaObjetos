# Definición de la clase base Video
class Video:
    def __init__(self, titulo, duracion):
        self._titulo = titulo  # Encapsulación: atributo protegido
        self._duracion = duracion  # Encapsulación: atributo protegido

    def reproducir(self):
        print(f"Reproduciendo {self._titulo}")

    def pausar(self):
        print(f"Pausando {self._titulo}")

    def detener(self):
        print(f"Deteniendo {self._titulo}")

    def obtener_informacion(self):
        return f"Título: {self._titulo}, Duración: {self._duracion} minutos"

# Definición de la clase Pelicula, que hereda de Video
class Pelicula(Video):
    def __init__(self, titulo, duracion, director):
        super().__init__(titulo, duracion)
        self._director = director  # Encapsulación: atributo protegido

    def obtener_informacion(self):
        info = super().obtener_informacion()
        return f"{info}, Director: {self._director}"

# Definición de la clase Serie, que hereda de Video
class Serie(Video):
    def __init__(self, titulo, duracion, temporada, episodio):
        super().__init__(titulo, duracion)
        self._temporada = temporada  # Encapsulación: atributo protegido
        self._episodio = episodio  # Encapsulación: atributo protegido

    def obtener_informacion(self):
        info = super().obtener_informacion()
        return f"{info}, Temporada: {self._temporada}, Episodio: {self._episodio}"

# Función principal para crear instancias y demostrar la funcionalidad
def main():
    pelicula1 = Pelicula("Inception", 148, "Christopher Nolan")
    serie1 = Serie("Breaking Bad", 47, 1, 1)

    lista_videos = [pelicula1, serie1]

    for video in lista_videos:
        video.reproducir()
        print(video.obtener_informacion())
        video.pausar()
        video.detener()
        print()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
