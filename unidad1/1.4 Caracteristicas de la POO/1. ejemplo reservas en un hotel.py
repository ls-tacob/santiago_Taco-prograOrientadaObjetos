class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Inicializa una habitación con un número, tipo y precio.

        :param numero: Número de la habitación
        :param tipo: Tipo de la habitación (e.g., simple, doble, suite)
        :param precio: Precio por noche de la habitación
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_ocupada = False  # Inicialmente, la habitación está disponible

    def __str__(self):
        return f'Habitación {self.numero} ({self.tipo}), Precio por noche: ${self.precio}, {"Ocupada" if self.esta_ocupada else "Disponible"}'


class Huesped:
    def __init__(self, nombre, documento):
        """
        Inicializa un huésped con un nombre y un documento de identificación.

        :param nombre: Nombre del huésped
        :param documento: Documento de identificación del huésped
        """
        self.nombre = nombre
        self.documento = documento

    def __str__(self):
        return f'Huésped {self.nombre}, Documento: {self.documento}'


class Reserva:
    def __init__(self, huesped, habitacion, noches):
        """
        Inicializa una reserva con un huésped, una habitación y la cantidad de noches.

        :param huesped: Objeto de tipo Huesped
        :param habitacion: Objeto de tipo Habitacion
        :param noches: Cantidad de noches de la reserva
        """
        self.huesped = huesped
        self.habitacion = habitacion
        self.noches = noches
        self.total = self.calcular_total()
        self.confirmar_reserva()

    def calcular_total(self):
        """
        Calcula el total a pagar por la reserva en función del precio por noche de la habitación y el número de noches.

        :return: Total a pagar
        """
        return self.habitacion.precio * self.noches

    def confirmar_reserva(self):
        """
        Marca la habitación como ocupada.
        """
        self.habitacion.esta_ocupada = True

    def __str__(self):
        return f'Reserva para {self.huesped.nombre} en {self.habitacion.tipo} (Habitación {self.habitacion.numero}) por {self.noches} noches. Total: ${self.total}'


# Creación de objetos de ejemplo
habitacion1 = Habitacion(101, 'Simple', 50)
habitacion2 = Habitacion(102, 'Doble', 80)
habitacion3 = Habitacion(103, 'Suite', 150)

huesped1 = Huesped('Carlos Pérez', '12345678')
huesped2 = Huesped('Ana Gómez', '87654321')

# Realización de reservas
reserva1 = Reserva(huesped1, habitacion1, 3)
reserva2 = Reserva(huesped2, habitacion3, 2)

# Ejemplo de salida
print(habitacion1)  # Debería mostrar que la habitación está ocupada
print(habitacion2)  # Debería mostrar que la habitación está disponible
print(habitacion3)  # Debería mostrar que la habitación está ocupada
print(huesped1)  # Información del huésped Carlos Pérez
print(huesped2)  # Información del huésped Ana Gómez
print(reserva1)  # Detalles de la reserva de Carlos Pérez
print(reserva2)  # Detalles de la reserva de Ana Gómez
