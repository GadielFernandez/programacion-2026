"""NIVEL 5 — Mi primera función: cargar las notas

SE PIDE
    Hasta ahora escribimos el código suelto. Desde este nivel lo guardamos en FUNCIONES para poder
    reutilizarlo: una función recibe datos (parámetros), hace un trabajo y devuelve el resultado con return.
    Convierta el nivel 1 en la función cargar_notas(ruta): lee el CSV de esa ruta y devuelve el DataFrame.
    Desde aquí empieza la CASCADA: los niveles siguientes llaman a esta función.

RESULTADO ESPERADO (con notas.csv)
    Filas: 15

NIVEL 5 · COMPLETAR LOS HUECOS. Hay dos: qué se lee (use el parámetro ruta) y qué se devuelve.
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_5_funcion_cargar.py
"""
import pandas as pd


def cargar_notas(ruta):
    """Lee el CSV y devuelve el DataFrame."""
    notas = pd.read_csv(____)      # use el parámetro de la función
    return ____                    # devuelva el DataFrame


if __name__ == "__main__":
    notas = cargar_notas("notas.csv")
    print("Filas:", len(notas))
