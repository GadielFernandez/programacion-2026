"""NIVEL 10 — Reporte final: todo en cascada

SE PIDE
    Reúna todo en un reporte. Devuelva un DICCIONARIO con cuatro datos:
      'estudiantes'        cantidad total de estudiantes
      'aprobados'          cantidad con promedio mayor o igual a 70
      'en_riesgo'          LISTA con los nombres de quienes tienen promedio < 65 y asistencia < 80
      'promedio_por_grupo' diccionario grupo → promedio, redondeado a 2 decimales
    Cada dato sale de una función que usted ya escribió en los niveles anteriores.

RESULTADO ESPERADO (con notas.csv)
    estudiantes 15 · aprobados 8 · en_riesgo: Diego Rojas, Mateo Araya, Andrés Calvo,
    Isabella Brenes, Lucía Jiménez · grupos: A 69.15, B 69.2, C 72.75

NIVEL 10 · RETO FINAL, SIN PISTAS. Aquí se ve la cascada completa: sus propias funciones
trabajando juntas. Si algo falla, el verificador le dirá qué nivel anterior revisar.
Ejecute desde la carpeta material_estudiante:  python 1_filtros_pandas/nivel_10_reporte.py
"""
import pandas as pd
from nivel_5_funcion_cargar import cargar_notas
from nivel_7_filtrar import aprobados
from nivel_8_dos_condiciones import en_riesgo
from nivel_9_agrupar import promedio_por_grupo


def generar_reporte(ruta):
    """Devuelve el diccionario con los cuatro datos del reporte."""
    # su código aquí
    return {}


if __name__ == "__main__":
    reporte = generar_reporte("notas.csv")
    print("Estudiantes:", reporte["estudiantes"])
    print("Aprobados:", reporte["aprobados"])
    print("En riesgo:", ", ".join(reporte["en_riesgo"]))
    print("Promedio por grupo:", reporte["promedio_por_grupo"])
