import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    # Diccionario de opciones organizadas por unidad
    opciones = {
        # unidad 1
        '1': {
            '1': 'unidad1/1.2 Técnicas de POO/combate.py',
            '2': 'unidad1/1.2 Técnicas de POO/guerrero.py',
            '3': 'unidad1/1.2 Técnicas de POO/mago.py',
            '4': 'unidad1/1.2 Técnicas de POO/personaje.py',
            '5': 'unidad1/1.3 programación tradicional frente a POO/1.temperaturaSemanal prograTradicional.py',
            '6': 'unidad1/1.3 programación tradicional frente a POO/2. temperaturaSemanal POO.py',
            '7': 'unidad1/1.3 programación tradicional frente a POO/3. temperaturaSemanal progamación tracicional frente a POO.py',
            '8': 'unidad1/1.4 Caracteristicas de la POO/1. ejemplo reservas en un hotel.py'
        },
        # unidad 2
        '2': {
            '9': 'unidad2/2.1 identificadores/programa de gestión de contactos.py',
            '10': 'unidad2/2.2 Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/main.py',
            '11': 'unidad2/2.2 Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/pelicula.py',
            '12': 'unidad2/2.2 Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/reproductor de video.py',
            '13': 'unidad2/2.2 Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/serie.py',
            '14': 'unidad2/2.2 Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/video.py',
            '15': 'unidad2/2.3 constructor y destructor/productos (constructor y destructor).py'
        }
    }

    while True:
        print("\nMenu Principal - Dashboard")
        print("Unidades disponibles:")
        for unidad in opciones:
            print(f"{unidad} - Unidad {unidad}")
        print("0 - Salir")

        unidad_elegida = input("Elige una unidad o '0' para salir: ")
        if unidad_elegida == '0':
            break
        elif unidad_elegida in opciones:
            while True:
                print(f"\nArchivos disponibles en Unidad {unidad_elegida}:")
                for key, value in opciones[unidad_elegida].items():
                    print(f"{key} - {value}")
                print("0 - Volver al menú principal")

                archivo_elegido = input("Elige un archivo para ver su código o '0' para volver: ")
                if archivo_elegido == '0':
                    break
                elif archivo_elegido in opciones[unidad_elegida]:
                    ruta_script = os.path.join(ruta_base, opciones[unidad_elegida][archivo_elegido])
                    mostrar_codigo(ruta_script)
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
