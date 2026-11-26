"""E08 — Pandas: dos condiciones

SE PIDE
    1) Ejecute el programa y anote el mensaje (o lo que sale mal).
    2) Clasifique el error, explique la causa con sus palabras y corríjalo.
    3) Compruebe que la salida coincide con la ESPERADA y anótelo en la bitácora.
    Ejecute desde la carpeta material_investigacion:  python A_errores/e08_pandas.py

SALIDA ESPERADA
    Cantidad: 2
"""
import pandas as pd

notas = pd.DataFrame({
    "nombre": ["Ana", "Beto", "Carla", "Dani"],
    "promedio": [80, 55, 92, 68],
    "asistencia": [90, 70, 95, 85],
})
# Estudiantes con promedio mayor a 70 Y asistencia mayor a 80
filtro = notas["promedio"] > 70 & notas["asistencia"] > 80
print("Cantidad:", len(notas[filtro]))
