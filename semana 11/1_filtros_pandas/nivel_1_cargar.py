"""NIVEL 1 — Cargar y mirar los datos

SE PIDE
    Lea el archivo notas.csv en una variable llamada notas. Un DataFrame es una tabla: cada fila
    es un estudiante y cada columna, un dato.

RESULTADO ESPERADO (con notas.csv)
    Filas: 15   y las columnas: cedula, nombre, grupo, tarea, practica, proyecto, examen, asistencia

NIVEL 1 · COMPLETAR EL HUECO. Cambie ____ por lo que corresponda (se hace igual que en la semana 10).
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_1_cargar.py
"""
import pandas as pd

# 1. Lea el archivo notas.csv y guárdelo en la variable notas
notas = pd.read_csv(____)

# 2. Mire los datos (estas líneas ya están listas)
print(notas.head(3))            # las primeras 3 filas
print("Filas:", len(notas))     # cuántos estudiantes hay
print("Columnas:", list(notas.columns))
