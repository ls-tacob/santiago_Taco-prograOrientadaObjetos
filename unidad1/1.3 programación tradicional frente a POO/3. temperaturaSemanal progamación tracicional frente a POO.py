# Programación Tradicional
# Ejemplo: Gestión de temperaturas diarias y cálculo del promedio semanal

# Definición de variables globales
temperaturas = [0] * 7  # Lista para almacenar las temperaturas diarias de una semana
dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Función para ingresar la temperatura diaria
def ingresar_temperatura(dia, temp):
    global temperaturas
    temperaturas[dia] = temp

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal():
    global temperaturas
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Uso de las funciones en la programación tradicional
ingresar_temperatura(0, 20)
ingresar_temperatura(1, 22)
ingresar_temperatura(2, 18)
ingresar_temperatura(3, 24)
ingresar_temperatura(4, 20)
ingresar_temperatura(5, 21)
ingresar_temperatura(6, 19)

promedio_temp = calcular_promedio_semanal()

# Imprimir las temperaturas diarias y el promedio semanal
print("Temperaturas Diarias (Tradicional):")
for i in range(7):
    print(f"{dias_de_la_semana[i]}: {temperaturas[i]}°C")

print(f"\nPromedio Semanal de Temperatura (Tradicional): {promedio_temp:.2f}°C")


# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de temperaturas diarias y cálculo del promedio semanal

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
        print("\nTemperaturas Diarias (POO):")
        for i in range(7):
            print(f"{self.dias_de_la_semana[i]}: {self.temperaturas[i]}°C")

    def mostrar_promedio_semanal(self):
        promedio = self.calcular_promedio_semanal()
        print(f"\nPromedio Semanal de Temperatura (POO): {promedio:.2f}°C")

# Crear una instancia de la clase Clima
clima = Clima()

# Uso de los métodos en la programación orientada a objetos
clima.ingresar_temperatura(0, 20)
clima.ingresar_temperatura(1, 22)
clima.ingresar_temperatura(2, 18)
clima.ingresar_temperatura(3, 24)
clima.ingresar_temperatura(4, 20)
clima.ingresar_temperatura(5, 21)
clima.ingresar_temperatura(6, 19)

# Mostrar las temperaturas diarias y el promedio semanal
clima.mostrar_temperaturas()
clima.mostrar_promedio_semanal()
