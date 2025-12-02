# src/act_1_io_basico.py
# ---------------------------------------------------------
# Actividad 1: Entrada / salida básica (print e input)
# Objetivo:
#   - Practicar impresiones en pantalla.
#   - Practicar captura de datos con input().
# ---------------------------------------------------------

from funciones import imprimir_nombre_completo


def demo_impresiones():
    """
    Demuestra impresiones sencillas con print
    y el uso de una función de apoyo.
    """
    print("=== Actividad 1: Demo de impresiones ===")

    # Ejemplo directo
    print("Hola   mundo")

    # Uso de variables con f-strings
    nombre = "Dilan"
    carrera = "ISC"
    print(f"{nombre} es de la carrera de {carrera}")

    # Uso de la función compartida para imprimir nombre completo
    imprimir_nombre_completo("Dilan Dariel", "Huerta Hernandes", "ISC")


def demo_input():
    """
    Demuestra el uso de input() y conversión
    de tipos de datos (int y float).
    """
    print("\n=== Actividad 1: Demo de input() ===")

    nombre = input("¿Cómo te llamas? ")
    edad = int(input("¿Cuántos años tienes? "))
    estatura = float(input("¿Cuál es tu estatura en cm? "))

    print(f"\nHola {nombre}, tienes {edad} años y mides {estatura} cm.")


def ejecutar():
    """
    Función principal de la actividad 1.
    Se manda llamar desde main.py
    """
    demo_impresiones()
    demo_input()


if __name__ == "__main__":
    # Permite probar esta actividad ejecutando solo este archivo.
    ejecutar()
