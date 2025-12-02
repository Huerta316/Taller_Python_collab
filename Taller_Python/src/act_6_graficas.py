# src/act_6_graficas.py
# ---------------------------------------------------------
# Actividad 6: Gráficas con matplotlib
# Objetivo:
#   - Graficar una relación temperatura vs tiempo.
#   - Graficar promedios por materia.
# ---------------------------------------------------------

import matplotlib.pyplot as plt


def grafica_temperatura():
    """
    Crea una gráfica de línea de temperatura vs tiempo.
    """
    print("\n=== Actividad 6: Gráfica Temperatura vs Tiempo ===")

    tiempo = [1, 4, 6, 8, 10, 12]           # eje X
    temperatura = [20, 23, 27, 25, 23, 19]  # eje Y

    plt.plot(tiempo, temperatura, marker="o")
    plt.xlabel("Tiempo (hrs)")
    plt.ylabel("Temperatura (°C)")
    plt.title("Temperatura vs Tiempo")
    plt.grid(True)
    plt.show()


def grafica_promedios_materias():
    """
    Crea una gráfica de barras con promedios por materia.
    """
    print("\n=== Actividad 6: Gráfica de promedios por materia ===")

    materias = ["Programación", "Física", "Geometría", "Cálculo"]
    promedios = [66, 55, 78, 92]

    plt.bar(materias, promedios)
    plt.ylabel("Promedio")
    plt.title("Promedio por materia")
    plt.show()


def ejecutar():
    """
    Función principal de la actividad 6.
    """
    grafica_temperatura()
    grafica_promedios_materias()


if __name__ == "__main__":
    ejecutar()
