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
