"""Microreto independiente: crear una función que limpie un nombre."""

# Diccionario de equivalencias de nombres de medicamentos
EQUIVALENCIAS = {
    "ACETAMINOFEN": "ACETAMINOFÉN",
    "PARACETAMOL": "ACETAMINOFÉN",
    "PANADOL": "ACETAMINOFÉN",
    "SALIR": "N"
}


def limpiar_nombre(nombre):
    """Devuelve nombre sin espacios en los extremos y en mayúsculas."""
    nombre = nombre.strip().upper()
    if nombre in EQUIVALENCIAS:
        nombre = EQUIVALENCIAS[nombre]
    return nombre


print(limpiar_nombre("  acetaminofén "))

# Pruebas con varios nombres
print(limpiar_nombre("ibuprofeno"))
print(limpiar_nombre("paracetamol"))
print(limpiar_nombre("amoxicilina"))
print(limpiar_nombre("PANADOL"))

medicamentos = []
while True:
    medicamento = input("Ingrese el nombre del medicamento (o 'n' para terminar): ")
    medicamento = limpiar_nombre(medicamento)

    if medicamento == "N":
        break
    medicamentos.append(medicamento)
    print(medicamentos)
    
    