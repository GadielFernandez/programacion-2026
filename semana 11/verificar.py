"""Verificador con retroalimentación. Calcula lo esperado sin Pandas y no muestra la solución.

    python verificar.py        revisa todo
    python verificar.py n3     revisa solo el nivel 3 de la etapa 1 (n1 a n10)
    python verificar.py e2     revisa la etapa 2 (traducir)

Ejecútelo desde la carpeta material_estudiante, cuantas veces quiera.
"""
import contextlib
import csv
import importlib.util
import io
import os
import runpy
import sys
from pathlib import Path

BASE = Path(__file__).parent
sys.path.insert(0, str(BASE / "1_filtros_pandas"))   # para que los niveles se importen entre sí
NOTAS = ["tarea", "practica", "proyecto", "examen"]
RUTA = str(BASE / "notas.csv")


def _leer():
    with open(BASE / "notas.csv", encoding="utf-8") as archivo:
        filas = list(csv.DictReader(archivo))
    for fila in filas:
        for clave in NOTAS + ["asistencia"]:
            fila[clave] = int(fila[clave])
        fila["promedio"] = sum(fila[c] for c in NOTAS) / 4
    return filas


def _cargar_modulo(nombre, ruta):
    especificacion = importlib.util.spec_from_file_location(nombre, BASE / ruta)
    modulo = importlib.util.module_from_spec(especificacion)
    especificacion.loader.exec_module(modulo)
    return modulo


def _ejecutar(ruta):
    """Ejecuta un archivo de código suelto (niveles 1 a 4) y devuelve sus variables."""
    antes = os.getcwd()
    os.chdir(BASE)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            return runpy.run_path(str(BASE / ruta), run_name="__main__")
    finally:
        os.chdir(antes)


def _prueba(nombre, funcion):
    try:
        mensaje = funcion()
    except NameError as error:
        print(f"  ✘ {nombre}: quedó un hueco sin completar ({error})")
        return False
    except Exception as error:  # el estudiante recibe el mensaje, no el traceback
        print(f"  ✘ {nombre}: error {type(error).__name__}: {error}")
        return False
    if mensaje is None:
        print(f"  ✔ {nombre}")
        return True
    print(f"  ✘ {nombre}: {mensaje}")
    return False


def _casi(a, b):
    return abs(float(a) - float(b)) < 0.01


def _dep(funcion, pd, filas):
    """True si el nivel del que depende este ya pasa."""
    try:
        return funcion(pd, filas) is None
    except Exception:
        return False


# ---------------------------------------------------------------- niveles 1 a 4: código suelto
def nivel_1(pd, filas):
    notas = _ejecutar("1_filtros_pandas/nivel_1_cargar.py").get("notas")
    if notas is None or not hasattr(notas, "columns"):
        return "la variable notas debe ser el DataFrame que lee notas.csv"
    if len(notas) != 15:
        return f"notas tiene {len(notas)} filas y debería tener 15"


def nivel_2(pd, filas):
    nombres = _ejecutar("1_filtros_pandas/nivel_2_una_columna.py").get("nombres")
    if nombres is None or hasattr(nombres, "columns"):
        return "la variable nombres debe ser UNA columna (una Series), no una tabla"
    if list(nombres) != [f["nombre"] for f in filas]:
        return "nombres no tiene los nombres de los estudiantes; ¿tomó la columna \"nombre\"?"


def nivel_3(pd, filas):
    resultado = _ejecutar("1_filtros_pandas/nivel_3_varias_columnas.py").get("resultado")
    if resultado is None or not hasattr(resultado, "columns"):
        return "la variable resultado debe ser una tabla con dos columnas"
    if list(resultado.columns) != ["nombre", "examen"]:
        return f"las columnas son {list(resultado.columns)} y debían ser ['nombre', 'examen']"


def nivel_4(pd, filas):
    variables = _ejecutar("1_filtros_pandas/nivel_4_calcular.py")
    for clave, columna in (("promedio_examen", "examen"), ("promedio_tarea", "tarea")):
        esperado = sum(f[columna] for f in filas) / len(filas)
        if not _casi(variables.get(clave, -1), esperado):
            return f"{clave} no coincide con el promedio de la columna {columna}"


# ---------------------------------------------------------------- niveles 5 a 10: funciones en cascada
DEP = "este nivel usa la función del nivel {} y ese nivel aún no pasa; revíselo primero con: python verificar.py n{}"


def nivel_5(pd, filas):
    m = _cargar_modulo("n5", "1_filtros_pandas/nivel_5_funcion_cargar.py")
    notas = m.cargar_notas(RUTA)
    if notas is None:
        return "devuelve None; ¿olvidó el return?"
    if len(notas) != 15:
        return f"devuelve {len(notas)} filas y deberían ser 15"


def nivel_6(pd, filas):
    if not _dep(nivel_5, pd, filas):
        return DEP.format(5, 5)
    m = _cargar_modulo("n6", "1_filtros_pandas/nivel_6_columna_nueva.py")
    notas = m.notas_con_promedio(RUTA)
    if notas is None or "promedio" not in notas.columns:
        return "no existe la columna 'promedio' en lo que devuelve"
    for i, f in enumerate(filas):
        if not _casi(notas["promedio"].iloc[i], f["promedio"]):
            return f"el promedio de la fila {i} no coincide; ¿usó las 4 notas y axis=1?"


def nivel_7(pd, filas):
    if not _dep(nivel_6, pd, filas):
        return DEP.format(6, 6)
    m = _cargar_modulo("n7", "1_filtros_pandas/nivel_7_filtrar.py")
    for minimo in (70, 90, 60):
        n = len(m.aprobados(RUTA, minimo))
        esperado = sum(1 for f in filas if f["promedio"] >= minimo)
        if n != esperado:
            return f"con minimo={minimo} devuelve {n} estudiantes; debería devolver {esperado}"


def nivel_8(pd, filas):
    if not _dep(nivel_6, pd, filas):
        return DEP.format(6, 6)
    m = _cargar_modulo("n8", "1_filtros_pandas/nivel_8_dos_condiciones.py")
    for nota, asistencia in ((65, 80), (75, 90), (50, 60)):
        n = len(m.en_riesgo(RUTA, nota, asistencia))
        esperado = sum(1 for f in filas if f["promedio"] < nota and f["asistencia"] < asistencia)
        if n != esperado:
            return f"con ({nota}, {asistencia}) devuelve {n} estudiantes; revise paréntesis y el operador que une las condiciones"


def nivel_9(pd, filas):
    if not _dep(nivel_6, pd, filas):
        return DEP.format(6, 6)
    m = _cargar_modulo("n9", "1_filtros_pandas/nivel_9_agrupar.py")
    serie = m.promedio_por_grupo(RUTA)
    if serie is None:
        return "devuelve None; ¿olvidó el return?"
    for g in "ABC":
        grupo = [f["promedio"] for f in filas if f["grupo"] == g]
        if not _casi(serie[g], sum(grupo) / len(grupo)):
            return f"el promedio del grupo {g} no coincide"


def nivel_10(pd, filas):
    pendientes = [str(n) for n, f in ((5, nivel_5), (7, nivel_7), (8, nivel_8), (9, nivel_9)) if not _dep(f, pd, filas)]
    if pendientes:
        return "este reporte usa los niveles anteriores; primero deben pasar: nivel " + ", nivel ".join(pendientes)
    m = _cargar_modulo("n10", "1_filtros_pandas/nivel_10_reporte.py")
    r = m.generar_reporte(RUTA)
    if not isinstance(r, dict):
        return "debe devolver un diccionario con las cuatro claves"
    faltan = {"estudiantes", "aprobados", "en_riesgo", "promedio_por_grupo"} - set(r)
    if faltan:
        return f"faltan claves: {sorted(faltan)}"
    if r["estudiantes"] != 15:
        return f"'estudiantes' vale {r['estudiantes']} y debería ser 15"
    if r["aprobados"] != sum(1 for f in filas if f["promedio"] >= 70):
        return "'aprobados' no coincide; ¿usó aprobados con el mínimo 70?"
    riesgo = [f["nombre"] for f in filas if f["promedio"] < 65 and f["asistencia"] < 80]
    if list(r["en_riesgo"]) != riesgo:
        return "'en_riesgo' debe ser una lista con los NOMBRES, en el orden del archivo"
    for g in "ABC":
        grupo = [f["promedio"] for f in filas if f["grupo"] == g]
        if g not in r["promedio_por_grupo"] or not _casi(r["promedio_por_grupo"][g], sum(grupo) / len(grupo)):
            return f"el promedio del grupo {g} no coincide"


# ---------------------------------------------------------------- etapa 2
def etapa_2(pd, filas):
    t = _cargar_modulo("e2", "2_traducir.py")
    df = pd.read_csv(BASE / "notas.csv")
    df["promedio"] = df[NOTAS].mean(axis=1)

    def a():
        n = t.contar_aprobados_pandas(df, 70)
        if int(n) != t.contar_aprobados_nativo(filas, 70):
            return f"devuelve {n}; debe coincidir con la versión nativa"

    def b():
        obtenido = t.promedio_examen_nativo(filas)
        esperado = sum(f["examen"] for f in filas) / len(filas)
        if abs(obtenido - esperado) > 0.01:
            return f"devuelve {obtenido}; revise el acumulador y la división"

    return [("contar_aprobados_pandas", a), ("promedio_examen_nativo", b)]


GRUPOS = [
    ("n1", "Etapa 1 · Nivel 1 — cargar", nivel_1),
    ("n2", "Etapa 1 · Nivel 2 — una columna", nivel_2),
    ("n3", "Etapa 1 · Nivel 3 — varias columnas", nivel_3),
    ("n4", "Etapa 1 · Nivel 4 — calcular", nivel_4),
    ("n5", "Etapa 1 · Nivel 5 — primera función", nivel_5),
    ("n6", "Etapa 1 · Nivel 6 — columna nueva", nivel_6),
    ("n7", "Etapa 1 · Nivel 7 — filtrar", nivel_7),
    ("n8", "Etapa 1 · Nivel 8 — dos condiciones", nivel_8),
    ("n9", "Etapa 1 · Nivel 9 — agrupar", nivel_9),
    ("n10", "Etapa 1 · Nivel 10 — reporte final", nivel_10),
    ("e2", "Etapa 2 — traducir", etapa_2),
]


def main():
    try:
        import pandas as pd
    except ImportError:
        print("Falta Pandas. Instálelo con:  python -m pip install pandas")
        return
    filas = _leer()
    pedido = sys.argv[1].lower() if len(sys.argv) > 1 else None
    if pedido and pedido not in {g[0] for g in GRUPOS}:
        print("Opciones: n1 a n10, e2 (o sin argumento para revisar todo)")
        return
    aprobadas = total = 0
    for clave, titulo, funcion in GRUPOS:
        if pedido and clave != pedido:
            continue
        print(titulo)
        if clave == "e2":
            for nombre, f in funcion(pd, filas):
                total += 1
                aprobadas += _prueba(nombre, f)
        else:
            total += 1
            aprobadas += _prueba(titulo.split("— ")[-1], lambda f=funcion: f(pd, filas))
    print(f"\n{aprobadas} de {total} pruebas aprobadas.")


if __name__ == "__main__":
    main()
