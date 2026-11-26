"""Verificador de la Investigación. Da una pista cuando algo falla; no entrega la solución.

    python verificar.py

Ejecútelo desde la carpeta material_investigacion, cuantas veces quiera.
"""
import csv
import importlib.util
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
ESPERADO = {
    'e01_sintaxis': 'Aprobado',
    'e02_nombre': 'Total: 4500',
    'e03_tipo': 'Hola Ana, tienes 17 años',
    'e04_indice': 'Promedio: 80.0',
    'e05_clave': 'Nombre: Luis\nGrupo: B',
    'e06_logico': 'Aprobados: 3',
    'e07_funcion': 'Promedio: 80.0',
    'e08_pandas': 'Cantidad: 2'}


def probar(nombre, funcion):
    try:
        mensaje = funcion()
    except Exception as error:
        print(f"  ✘ {nombre}: error {type(error).__name__}: {error}")
        return False
    if mensaje is None:
        print(f"  ✔ {nombre}")
        return True
    print(f"  ✘ {nombre}: {mensaje}")
    return False


def revisar_error(nombre):
    ruta = BASE / "A_errores" / f"{nombre}.py"
    r = subprocess.run([sys.executable, str(ruta)], capture_output=True, text=True, timeout=30, cwd=BASE)
    if r.returncode != 0:
        ultima = (r.stderr.strip().splitlines() or ["(sin mensaje)"])[-1]
        return f"todavía falla: {ultima}"
    if r.stdout.strip() != ESPERADO[nombre]:
        return "ya no da error, pero la salida no coincide con la ESPERADA del encabezado"


def revisar_reto():
    import pandas as pd
    especificacion = importlib.util.spec_from_file_location("reto", BASE / "reto.py")
    reto = importlib.util.module_from_spec(especificacion)
    especificacion.loader.exec_module(reto)
    with open(BASE / "notas.csv", encoding="utf-8") as archivo:
        filas = list(csv.DictReader(archivo))
    # Se prueba con los datos originales y con los exámenes +10, para comprobar la lógica
    for extra in (0, 10):
        notas = [int(f["examen"]) + extra for f in filas if f["grupo"] == "B"]
        cantidad = sum(1 for n in notas if n >= 70)
        promedio = round(sum(notas) / len(notas), 2)
        df = pd.read_csv(BASE / "notas.csv")
        df["examen"] = df["examen"] + extra
        obtenido = reto.resumen_grupo_b(df)
        if not isinstance(obtenido, tuple):
            return "debe devolver una TUPLA (cantidad, promedio)"
        if int(obtenido[0]) != cantidad:
            return f"la cantidad es {obtenido[0]}; revise el grupo y la condición (mayor o igual a 70)"
        if abs(float(obtenido[1]) - promedio) > 0.01:
            return f"el promedio es {obtenido[1]}; ¿lo calculó sobre todo el grupo B y redondeó a 2 decimales?"


def main():
    aprobadas = 0
    print("Parte A — errores corregidos")
    for nombre in ESPERADO:
        aprobadas += probar(nombre, lambda n=nombre: revisar_error(n))
    print("Parte B — reto")
    aprobadas += probar("reto", revisar_reto)
    print(f"\n{aprobadas} de {len(ESPERADO) + 1} pruebas aprobadas.")


if __name__ == "__main__":
    main()
