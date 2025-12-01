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
- Organización del código en módulos (`src/`)

---

## Estructura del repositorio

```text
.
├── src/
│   ├── main.py                   # Programa principal con menú de demostración
│   ├── funciones.py              # Funciones auxiliares reutilizables
│   ├── io_basico.py              # Ejemplos de entrada/salida e impresiones
│   ├── estructuras_control.py    # If / for / while y promedio de listas
│   ├── analisis_datos.py         # Uso de pandas + numpy con datos de calificaciones
│   └── graficas.py               # Gráficas con matplotlib
│
├── data/
│   ├── tb_movies.csv             # Datos de ejemplo para pandas
│   └── datos.xlsx                # Calificaciones de ejemplo (parciales)
│
├── notebooks/
│   └── Taller_Huerta_Dilan.ipynb   # Cuaderno de Google Colab exportado
│
├── requirements.txt              # Dependencias del proyecto
├── README.md                     # Este archivo
└── .gitignore                    # Archivos/carpetas ignorados por git
