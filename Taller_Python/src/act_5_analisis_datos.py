# src/act_5_analisis_datos.py
# ---------------------------------------------------------
# Actividad 5: Análisis de datos con pandas y numpy
# Objetivo:
#   - Leer un archivo Excel con pandas.
#   - Calcular el promedio de 3 parciales.
#   - Asignar estatus "Aprobado" o "Reprobado".
#   - Guardar un archivo modificado.
# ---------------------------------------------------------

import pandas as pd
import numpy as np


def cargar_y_mostrar():
    """
    Lee el archivo datos.xlsx y muestra
    las primeras filas y descripción estadística.
    """
    print("\n=== Actividad 5: Lectura de datos.xlsx ===")
    df = pd.read_excel("data/datos.xlsx")
    print("\nPrimeras filas del archivo:")
    print(df.head())
    print("\nDescripción rápida (describe):")
    print(df.describe())


def calcular_promedio_y_estatus():
    """
    Calcula el promedio de los parciales y el estatus,
    y guarda el resultado en datos_mod.xlsx.
    """
    print("\n=== Actividad 5: Cálculo de promedio y estatus ===")
    df = pd.read_excel("data/datos.xlsx")

    # Calcula el promedio entre columnas de parciales
    df["prom"] = df[["Parcial 1", "Parcial 2", "Parcial 3"]].mean(axis=1)

    # Asigna estatus según el promedio
    df["estatus"] = np.where(df["prom"] >= 7, "Aprobado", "Reprobado")

    print("\nDatos con promedio y estatus:")
    print(df)

    # Guarda el DataFrame modificado en un nuevo archivo
    df.to_excel("data/datos_mod.xlsx", index=False)
    print("\nArchivo guardado como data/datos_mod.xlsx")


def ejecutar():
    """
    Función principal de la actividad 5.
    """
    cargar_y_mostrar()
    calcular_promedio_y_estatus()


if __name__ == "__main__":
    ejecutar()
