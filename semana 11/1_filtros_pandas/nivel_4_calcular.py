"""NIVEL 4 — Calcular sobre una columna

SE PIDE
    Calcule el promedio de la columna examen y, usted solo, el de la columna tarea.

RESULTADO ESPERADO (con notas.csv)
    Examen: 68.67   (aprox.)      Tarea: 69.93   (aprox.)

NIVEL 4 · HUECOS Y UN PASO SOLO. En el 1 hay dos huecos: qué columna se toma (nivel 2) y qué
cálculo se hace (el promedio de una columna se llama mean). El 2 lo escribe usted.
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_4_calcular.py
"""
import pandas as pd

notas = pd.read_csv("notas.csv")

# 1. Promedio de la columna examen (complete los dos huecos)
promedio_examen = notas[____].____()

# 2. Ahora usted solo: promedio de la columna tarea
promedio_tarea = 0      # reemplace el 0 por su código

# 3. Mire los resultados (estas líneas ya están listas)
print("Examen:", round(promedio_examen, 2))
print("Tarea:", round(promedio_tarea, 2))
