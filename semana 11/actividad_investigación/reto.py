"""Investigación, Parte B — Reto

SE PIDE
    Complete resumen_grupo_b(df). Debe devolver una TUPLA (cantidad, promedio):
      - cantidad: estudiantes del grupo B con examen mayor o igual a 70
      - promedio: promedio del examen de TODO el grupo B, con 2 decimales
    Pista: filtre el grupo con df[df["grupo"] == "B"] y trabaje sobre ese resultado.

Ejecute desde la carpeta material_investigacion:  python reto.py
"""
import pandas as pd


def resumen_grupo_b(df):
    """Devuelve (cantidad, promedio) del grupo B."""
    # su código aquí
    return (0, 0.0)


if __name__ == "__main__":
    notas = pd.read_csv("notas.csv")
    print("Resultado:", resumen_grupo_b(notas))
