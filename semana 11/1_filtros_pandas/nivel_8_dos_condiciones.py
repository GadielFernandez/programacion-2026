"""NIVEL 8 — Combinar dos condiciones (en cascada)

SE PIDE
    Devuelva los estudiantes en riesgo: 'promedio' MENOR que 'nota_maxima' Y 'asistencia' MENOR que
    'asistencia_minima'. Igual que en el nivel 7, el promedio sale de la función del nivel 6.

RESULTADO ESPERADO (con notas.csv)
    Con (65, 80)  →  5 estudiantes: Diego, Mateo, Andrés, Isabella y Lucía

NIVEL 8 · SIN PISTAS (solo recuerde que funciona en cascada con el nivel 6).
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_8_dos_condiciones.py
"""
import pandas as pd
from nivel_6_columna_nueva import notas_con_promedio


def en_riesgo(ruta, nota_maxima, asistencia_minima):
    """Estudiantes con promedio y asistencia bajos a la vez."""
    notas = notas_con_promedio(ruta)    # cascada: nivel 6
    # su código aquí
    return notas


if __name__ == "__main__":
    resultado = en_riesgo("notas.csv", 65, 80)
    print(resultado[["nombre", "promedio", "asistencia"]])
