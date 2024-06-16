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
for i in range(7):
    temp = float(input(f"Ingrese la temperatura para {dias_de_la_semana[i]}: "))
    ingresar_temperatura(i, temp)

promedio_temp = calcular_promedio_semanal()

# Imprimir las temperaturas diarias y el promedio semanal
print("\nTemperaturas Diarias:")
for i in range(7):
    print(f"{dias_de_la_semana[i]}: {temperaturas[i]}°C")

print(f"\nPromedio Semanal de Temperatura: {promedio_temp:.2f}°C")
