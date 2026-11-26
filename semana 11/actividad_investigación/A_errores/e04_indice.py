"""E04 — Listas y ciclos

SE PIDE
    1) Ejecute el programa y anote el mensaje (o lo que sale mal).
    2) Clasifique el error, explique la causa con sus palabras y corríjalo.
    3) Compruebe que la salida coincide con la ESPERADA y anótelo en la bitácora.
    Ejecute desde la carpeta material_investigacion:  python A_errores/e04_indice.py

SALIDA ESPERADA
    Promedio: 80.0
"""
notas = [80, 90, 70]
total = 0
for i in range(len(notas) + 1):
    total += notas[i]
print("Promedio:", total / len(notas))
