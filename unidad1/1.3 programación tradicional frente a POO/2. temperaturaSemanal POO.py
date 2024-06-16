class Clima:
    def __init__(self):
        self.temperaturas = [0] * 7  # Lista para almacenar las temperaturas diarias de una semana
        self.dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def ingresar_temperatura(self, dia, temp):
        self.temperaturas[dia] = temp

    def calcular_promedio_semanal(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

    def mostrar_temperaturas(self):
        print("\nTemperaturas Diarias:")
        for i in range(7):
            print(f"{self.dias_de_la_semana[i]}: {self.temperaturas[i]}°C")

    def mostrar_promedio_semanal(self):
        promedio = self.calcular_promedio_semanal()
        print(f"\nPromedio Semanal de Temperatura: {promedio:.2f}°C")

# Crear una instancia de la clase Clima
clima = Clima()

# Uso de los métodos en la programación orientada a objetos
for i in range(7):
    temp = float(input(f"Ingrese la temperatura para {clima.dias_de_la_semana[i]}: "))
    clima.ingresar_temperatura(i, temp)

# Mostrar las temperaturas diarias y el promedio semanal
clima.mostrar_temperaturas()
clima.mostrar_promedio_semanal()
