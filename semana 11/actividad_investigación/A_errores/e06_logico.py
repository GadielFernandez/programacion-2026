"""E06 — Condiciones: error SIN mensaje

SE PIDE
    1) Ejecute el programa y anote el mensaje (o lo que sale mal).
    2) Clasifique el error, explique la causa con sus palabras y corríjalo.
    3) Compruebe que la salida coincide con la ESPERADA y anótelo en la bitácora.
    Ejecute desde la carpeta material_investigacion:  python A_errores/e06_logico.py

SALIDA ESPERADA
    Aprobados: 3
"""
notas = [70, 55, 90, 70, 40]
aprobados = 0
for nota in notas:
    if nota > 70:
        aprobados += 1
print("Aprobados:", aprobados)
