# src/main.py
# ---------------------------------------------------------
# Menú principal del taller de Python.
# Desde aquí se puede ejecutar cada actividad act_1 ... act_6.
# ---------------------------------------------------------

import act_1_io_basico
import act_2_estructuras_control
import act_3_listas_promedios
import act_4_pares_impares
import act_5_analisis_datos
import act_6_graficas


def main():
    while True:
        print("\n=====================================")
        print("  Taller Python - Menú de actividades")
        print("=====================================")
        print("1) Actividad 1: Entrada / salida básica")
        print("2) Actividad 2: Estructuras de control (if / for / while)")
        print("3) Actividad 3: Listas y promedio de calificaciones")
        print("4) Actividad 4: Pares / impares (15 números)")
        print("5) Actividad 5: Análisis de datos (pandas / numpy)")
        print("6) Actividad 6: Gráficas con matplotlib")
        print("7) Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            act_1_io_basico.ejecutar()
        elif opcion == "2":
            act_2_estructuras_control.ejecutar()
        elif opcion == "3":
            act_3_listas_promedios.ejecutar()
        elif opcion == "4":
            act_4_pares_impares.ejecutar()
        elif opcion == "5":
            act_5_analisis_datos.ejecutar()
        elif opcion == "6":
            act_6_graficas.ejecutar()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
