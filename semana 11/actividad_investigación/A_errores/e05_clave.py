"""E05 — Diccionarios

SE PIDE
    1) Ejecute el programa y anote el mensaje (o lo que sale mal).
    2) Clasifique el error, explique la causa con sus palabras y corríjalo.
    3) Compruebe que la salida coincide con la ESPERADA y anótelo en la bitácora.
    Ejecute desde la carpeta material_investigacion:  python A_errores/e05_clave.py

SALIDA ESPERADA
    Nombre: Luis
    Grupo: B
"""
estudiante = {"nombre": "Luis", "edad": 18, "grupo": "B"}
print("Nombre:", estudiante["nombre"])
print("Grupo:", estudiante["Grupo"])
