"""NIVEL 9 — Agrupar y calcular por grupo (en cascada)

SE PIDE
    Devuelva el promedio de la columna 'promedio' para cada grupo (A, B y C).
    El promedio de cada estudiante sale de la función del nivel 6.

RESULTADO ESPERADO (con notas.csv)
    A 69.15   B 69.20   C 72.75

NIVEL 9 · SIN PISTAS (solo recuerde que funciona en cascada con el nivel 6).
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_9_agrupar.py
"""
import pandas as pd
from nivel_6_columna_nueva import notas_con_promedio


def promedio_por_grupo(ruta):
    """Promedio de 'promedio' en cada grupo."""
    notas = notas_con_promedio(ruta)    # cascada: nivel 6
    # su código aquí
    return None


if __name__ == "__main__":
    print(promedio_por_grupo("notas.csv").round(2))
