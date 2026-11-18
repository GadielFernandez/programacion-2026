"""El mismo expediente, con Pandas y las mismas tres funciones."""

from pathlib import Path
import pandas as pd
# Aquí importaremos pandas (ej. import pandas as pd).

ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
    """Decisión 1: ¿qué leímos y cuántas atenciones hay?"""
    # Contamos las filas del DataFrame y mostramos los nombres de sus columnas.
    print("Atenciones: ", len(atenciones))
    print("Campos:", list(atenciones.columns))


def contar_categorias(atenciones):
    """Decisión 2: ¿qué medicamentos, hospitales y diagnósticos aparecen?"""
    # Contamos la frecuencia de cada medicamento, hospital y diagnóstico usando Pandas.
    print("Medicamentos:", atenciones["medicamento"].value_counts().to_dict())
    print("\nHospitales:\n", atenciones['hospital'].value_counts())
    print("\nDiagnosticos:\n", atenciones['diagnostico'].value_counts())


def concluir(atenciones):
    """Decisiones 3 y 4: ¿cuántas personas hay y cuánto esperaron?"""
    # Contamos personas únicas por cédula, visitas por persona, total y promedio de espera.
    print("\nPersonas: ", atenciones['cedula'].nunique())
    print("Visita", atenciones['cedula'].value_counts())
    print("\nMinutos de espera:", atenciones['minutos_espera'].sum())
    print("Promedio:", atenciones['minutos_espera'].mean())

try:
    # Leemos el CSV con pd.read_csv(ARCHIVO_CSV). Se usa SimpleNamespace(empty=True) para evitar error.
    atenciones = pd.read_csv(ARCHIVO_CSV)
    print("Tipo :", type(atenciones))
    #print(atenciones)
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")
