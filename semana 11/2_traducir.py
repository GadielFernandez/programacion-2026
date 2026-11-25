"""Parte 3 — Traducir entre los dos lentes.

Cada ejercicio trae una versión resuelta y usted escribe la otra.
Use SU propio código; verificar.py comprueba el resultado.
"""
import pandas as pd


# --- Ejercicio A: de Python nativo a Pandas ----------------------------
def contar_aprobados_nativo(filas: list, minimo: float) -> int:
    """Versión resuelta. 'filas' es una lista de diccionarios con 'promedio'."""
    cantidad = 0
    for fila in filas:
        if fila["promedio"] >= minimo:
            cantidad += 1
    return cantidad


def contar_aprobados_pandas(df: pd.DataFrame, minimo: float) -> int:
    """TODO: haga lo mismo con Pandas, en una sola línea."""
    return 0


# --- Ejercicio B: de Pandas a Python nativo ----------------------------
def promedio_examen_pandas(df: pd.DataFrame) -> float:
    """Versión resuelta."""
    return df["examen"].mean()


def promedio_examen_nativo(filas: list) -> float:
    """TODO: haga lo mismo con un ciclo for y un acumulador.
    'filas' es una lista de diccionarios con la clave 'examen'."""
    return 0.0
