"""El mismo expediente, con Pandas y las mismas tres funciones."""

from pathlib import Path

import pandas as pd


ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
    print("Atenciones:", len(atenciones))
    print("Campos:", list(atenciones.columns))


def contar_categorias(atenciones):
    print("Medicamentos:", atenciones["medicamento"].value_counts().to_dict())
    print("Hospitales:", atenciones["hospital"].value_counts().to_dict())
    print("Diagnósticos:", atenciones["diagnostico"].value_counts().to_dict())


def concluir(atenciones):
    print("Visitas por cédula:", atenciones["cedula"].value_counts().to_dict())
    print("Personas:", atenciones["cedula"].nunique())
    print("Minutos de espera:", atenciones["minutos_espera"].sum())
    print("Promedio:", atenciones["minutos_espera"].mean())


try:
    atenciones = pd.read_csv(ARCHIVO_CSV, encoding="utf-8-sig", dtype={"cedula": str})
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")
