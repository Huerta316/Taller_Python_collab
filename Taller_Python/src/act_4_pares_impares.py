# src/act_4_pares_impares.py
# ---------------------------------------------------------
# Actividad 4:
#   - Capturar 15 números.
#   - Contar cuántos son pares.
#   - Convertir los impares a pares (sumando 1).
#   - Imprimir la lista resultante.
# ---------------------------------------------------------

from funciones import contar_pares_y_convertir


def ejecutar():
    """
    Función principal de la actividad 4.
    """
    print("\n=== Actividad 4: Pares e impares ===")

    numeros = []
    for i in range(15):
        n = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(n)

    cantidad_pares, lista_convertida = contar_pares_y_convertir(numeros)

    print("\nNúmeros ingresados:", numeros)
    print("Cantidad de pares:", cantidad_pares)
    print("Lista con impares convertidos a pares:", lista_convertida)


if __name__ == "__main__":
    ejecutar()
