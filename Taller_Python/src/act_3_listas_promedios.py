# src/act_3_listas_promedios.py
# ---------------------------------------------------------
# Actividad 3: Listas y promedio
# Objetivo:
#   - Crear listas.
#   - Recorrer listas con for.
#   - Calcular el promedio de calificaciones.
# ---------------------------------------------------------

from funciones import promedio_lista


def demo_lista_fija():
    """
    Usa una lista fija de calificaciones
    y calcula el promedio de dos formas.
    """
    print("\n=== Actividad 3: Lista fija de calificaciones ===")
    calif = [4, 6, 9, 7, 5]
    print("Calificaciones:", calif)

    # Promedio usando la función promedio_lista (suma/len)
    prom = promedio_lista(calif)
    print("Promedio usando función:", prom)

    # Promedio usando for y range (versión más detallada)
    suma = 0
    for i in range(len(calif)):
        suma += calif[i]

    prom2 = suma / len(calif)
    print("Promedio usando for + range:", prom2)


def demo_lista_usuario():
    """
    Permite al usuario capturar una lista de números
    y muestra la lista final.
    """
    print("\n=== Actividad 3: Lista capturada por el usuario ===")

    cantidad = int(input("¿Cuántos datos deseas capturar? "))

    lista = []
    for i in range(cantidad):
        valor = int(input(f"Valor {i + 1}: "))
        lista.append(valor)

    print("\nLista capturada:", lista)

    if len(lista) > 0:
        prom = promedio_lista(lista)
        print("Promedio de la lista:", prom)
    else:
        print("La lista está vacía, no se puede calcular el promedio.")


def ejecutar():
    """
    Función principal de la actividad 3.
    """
    demo_lista_fija()
    demo_lista_usuario()


if __name__ == "__main__":
    ejecutar()
