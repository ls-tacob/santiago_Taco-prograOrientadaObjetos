class Evento:
    def __init__(self, fecha, hora, descripcion, estado):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"{self.fecha} {self.hora}: {self.descripcion} - {self.estado}"
