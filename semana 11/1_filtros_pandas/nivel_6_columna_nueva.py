"""NIVEL 6 — Una columna nueva a partir de otras (en cascada)

SE PIDE
    Devuelva las notas con una columna nueva 'promedio': la media de tarea, practica, proyecto y
    examen de CADA estudiante. Para leer el archivo use la función del nivel 5.

RESULTADO ESPERADO (con notas.csv)
    Valeria 88.75   Diego 53.25   Camila 74.25

NIVEL 6 · SOLO UNA PISTA. Funciona EN CASCADA: llama a cargar_notas (nivel 5). Tome las cuatro
columnas como en el nivel 3, y .mean(axis=1) calcula el promedio de cada FILA (axis=1 = "a lo ancho").
Una columna nueva se crea así: notas["nombre_nuevo"] = ...
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_6_columna_nueva.py
"""
import pandas as pd
from nivel_5_funcion_cargar import cargar_notas


def notas_con_promedio(ruta):
    """Notas con la columna 'promedio'."""
    notas = cargar_notas(ruta)    # cascada: usamos la función del nivel 5
    # su código aquí
    return notas


if __name__ == "__main__":
    notas = notas_con_promedio("notas.csv")
    print(notas[["nombre", "promedio"]].head(3))
