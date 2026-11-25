"""NIVEL 7 — Filtrar con una condición (en cascada)

SE PIDE
    Devuelva solo los estudiantes cuyo 'promedio' sea mayor o igual que 'minimo'.
    El promedio ya lo calcula la función del nivel 6.

RESULTADO ESPERADO (con notas.csv)
    Con minimo = 70  →  8 estudiantes

NIVEL 7 · SOLO UNA PISTA. Funciona EN CASCADA: llama a notas_con_promedio (nivel 6). Una condición
como notas["promedio"] >= 70 da True o False por fila; dentro de notas[...] queda solo lo que cumple.
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_7_filtrar.py
"""
import pandas as pd
from nivel_6_columna_nueva import notas_con_promedio


def aprobados(ruta, minimo):
    """Estudiantes con promedio mayor o igual que 'minimo'."""
    notas = notas_con_promedio(ruta)    # cascada: nivel 6
    # su código aquí
    return notas


if __name__ == "__main__":
    resultado = aprobados("notas.csv", 70)
    print("Estudiantes:", len(resultado))
