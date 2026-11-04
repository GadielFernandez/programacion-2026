"""Lectura preparada para la clase. El estudiantado no modifica este archivo.

Descarga registros y equivalencias desde el repositorio público. Si alguna
lectura falla, usa las dos copias locales para no mezclar versiones.
"""

import json
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


URL_BASE = (
    "https://api.github.com/repos/amenaactppp/td10-datos-publicos/"
    "contents/datos/"
)
CARPETA = Path(__file__).resolve().parent


def leer_api(nombre):
    solicitud = Request(
        URL_BASE + nombre + "?ref=main",
        headers={
            "Accept": "application/vnd.github.raw+json",
            "User-Agent": "TD10-Semana08-Clase",
            "Cache-Control": "no-cache",
        },
    )
    with urlopen(solicitud, timeout=10) as respuesta:
        return json.load(respuesta)


def leer_respaldo():
    with (CARPETA / "datos_respaldo.json").open(encoding="utf-8") as archivo:
        registros = json.load(archivo)
    with (CARPETA / "equivalencias_respaldo.json").open(encoding="utf-8") as archivo:
        equivalencias = json.load(archivo)
    return registros, equivalencias, "copia local de respaldo"


def cargar_datos(usar_respaldo=False):
    """Devuelve registros, equivalencias y el origen de ambos JSON."""
    if usar_respaldo:
        return leer_respaldo()
    try:
        registros = leer_api("registros.json")
        equivalencias = leer_api("equivalencias.json")
        if not isinstance(registros, list) or not isinstance(equivalencias, dict):
            raise ValueError("la respuesta no tiene la estructura esperada")
        if any(
            not isinstance(registro, dict)
            or "codigo" not in registro
            or not all(
                isinstance(registro.get(campo), str) and registro[campo].strip()
                for campo in (
                    "hospital", "paciente_id", "paciente_nombre",
                    "paciente_cedula", "grupo_edad", "diagnostico",
                )
            )
            or not isinstance(registro.get("medicamentos"), list)
            for registro in registros
        ):
            raise ValueError("los registros no tienen la estructura esperada")
        return registros, equivalencias, "JSON públicos de GitHub"
    except (URLError, TimeoutError, json.JSONDecodeError, ValueError) as error:
        print("Aviso: no se pudo leer la API:", error)
        return leer_respaldo()
