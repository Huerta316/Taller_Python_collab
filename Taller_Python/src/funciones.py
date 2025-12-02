# src/act_2_estructuras_control.py
# ---------------------------------------------------------
# Actividad 2: Estructuras de control
# Objetivo:
#   - Usar condicionales if / elif / else.
#   - Practicar ciclos for y while.
#   - Resolver una mini calculadora.
# ---------------------------------------------------------

from funciones import calculadora_basica


def demo_calculadora():
    """
    Calculadora básica que pide dos números
    y permite elegir la operación con un menú.
    """
    print("\n=== Actividad 2: Calculadora con if ===")

    x = int(input("Primer valor: "))
    y = int(input("Segundo valor: "))

    print("\n¿Qué operación deseas?")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")

    op = int(input("Opción: "))

    try:
        resultado = calculadora_basica(x, y, op)
        print("Resultado:", resultado)
    except ValueError as e:
        print("Error:", e)


def demo_for_while():
    """
    Ejemplos sencillos de uso de for y while.
    """
    print("\n=== Actividad 2: Ciclos for y while ===")

    print("\nFor de 0 a 9:")
    for i in range(10):
        print(i)

    print("\nFor de 1 a 10 de 3 en 3:")
    for i in range(1, 11, 3):
        print(i)

    print("\nWhile de 0 a 4:")
    contador = 0
    while contador < 5:
        print(f"Contador: {contador}")
        contador += 1


def ejecutar():
    """
    Función principal de la actividad 2.
    """
    demo_calculadora()
    demo_for_while()


if __name__ == "__main__":
    ejecutar()
