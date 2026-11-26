"""E07 — Funciones: error SIN mensaje

SE PIDE
    1) Ejecute el programa y anote el mensaje (o lo que sale mal).
    2) Clasifique el error, explique la causa con sus palabras y corríjalo.
    3) Compruebe que la salida coincide con la ESPERADA y anótelo en la bitácora.
    Ejecute desde la carpeta material_investigacion:  python A_errores/e07_funcion.py

SALIDA ESPERADA
    Promedio: 80.0
"""
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3


resultado = calcular_promedio(80, 90, 70)
print("Promedio:", resultado)
