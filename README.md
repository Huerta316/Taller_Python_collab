# Taller “Python para la Ciencia, Tecnología e Ingeniería”

Este repositorio contiene el material desarrollado para la evaluación del taller **Python para la Ciencia, Tecnología e Ingeniería**.  

Incluye ejercicios de:

- Entrada y salida de datos con `input()`
- Manejo de variables y operaciones aritméticas
- Estructuras de control (`if`, `for`, `while`)
- Funciones
- Uso de paquetes científicos: `numpy`, `pandas`, `matplotlib`
- Lectura y escritura de archivos CSV/Excel
- Generación de gráficas sencillas
- Organización del código en módulos y actividades (`act_1`, `act_2`, ...)

---

## Estructura del repositorio

```text
.
├── src/
│   ├── main.py                        # Menú principal del taller
│   ├── funciones.py                   # Funciones reutilizables (promedios, calculadora, etc.)
│   ├── act_1_io_basico.py             # Actividad 1: impresiones e input()
│   ├── act_2_estructuras_control.py   # Actividad 2: if / for / while y calculadora
│   ├── act_3_listas_promedios.py      # Actividad 3: listas y promedio de calificaciones
│   ├── act_4_pares_impares.py         # Actividad 4: conteo de pares e impares (15 números)
│   ├── act_5_analisis_datos.py        # Actividad 5: análisis de datos con pandas / numpy
│   └── act_6_graficas.py              # Actividad 6: gráficas con matplotlib
│
├── data/
│   ├── tb_movies.csv                  # Datos de ejemplo para pandas
│   └── datos.xlsx                     # Calificaciones de ejemplo (parciales)
│
├── notebooks/
│   └── Taller_Huerta_Dilan.ipynb   # Cuaderno de Google Colab exportado
│
├── requirements.txt                   # Dependencias del proyecto
├── README.md                          # Este archivo
└── .gitignore                         # Archivos/carpetas ignorados por git
