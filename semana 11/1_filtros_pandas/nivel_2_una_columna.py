"""NIVEL 2 — Seleccionar UNA columna

SE PIDE
    Tome solo la columna nombre y guárdela en la variable nombres. Una columna se pide con su
    nombre entre comillas dentro de corchetes: notas["columna"].

RESULTADO ESPERADO (con notas.csv)
    Valeria Mora, Diego Rojas, Camila Soto   y   Tipo: Series (una columna es una Series)

NIVEL 2 · COMPLETAR EL HUECO. Falta el nombre de la columna.
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_2_una_columna.py
"""
import pandas as pd

notas = pd.read_csv("notas.csv")

# 1. Seleccione la columna "nombre" y guárdela en la variable nombres
nombres = notas[____]

# 2. Mire el resultado (estas líneas ya están listas)
print(nombres.head(3))
print("Tipo:", type(nombres).__name__)
