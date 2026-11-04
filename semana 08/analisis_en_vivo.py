"""
SEMANA 8 - EL ARCHIVO ESTA VIVO
Analisis de datos de una red hospitalaria.

Universidad Castro Carazo
"""

from fuente import cargar_datos

# ------------------------------------------------
# 1. CARGAR LOS DATOS
# ------------------------------------------------

USAR_RESPALDO = False

registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)

print("=" * 60)
print("INFORME DE ANALISIS - SEMANA 8")
print("=" * 60)

print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))


# ------------------------------------------------
# 2. MOSTRAR UNA MUESTRA DE HASTA TRES REGISTROS
# ------------------------------------------------

print("\n1. MUESTRA DE REGISTROS")

for posicion in range(min(3, len(registros))):

    registro = registros[posicion]

    print("\nRegistro:", posicion + 1)
    print("Codigo:", registro["codigo"])
    print("Hospital:", registro["hospital"])
    print("Paciente:", registro["paciente_nombre"])
    print("Cedula:", registro["paciente_cedula"])
    print("Diagnostico:", registro["diagnostico"])
    print("Medicamentos:", registro["medicamentos"])


# ------------------------------------------------
# 3. CONTEO LITERAL DE MEDICAMENTOS
# ------------------------------------------------

print("\n2. CONTEO LITERAL")

conteo_literal = {}
total_menciones = 0

for registro in registros:

    for medicamento in registro["medicamentos"]:

        if medicamento not in conteo_literal:
            conteo_literal[medicamento] = 0

        conteo_literal[medicamento] += 1
        total_menciones += 1

for medicamento, cantidad in conteo_literal.items():
    print(medicamento, ":", cantidad)

print("Total de menciones:", total_menciones)


# ------------------------------------------------
# 4. CONTEO NORMALIZADO
# ------------------------------------------------

print("\n3. CONTEO NORMALIZADO")

conteo_normalizado = {}

for registro in registros:

    for medicamento in registro["medicamentos"]:

        nombre = medicamento.strip().casefold()

        if nombre not in conteo_normalizado:
            conteo_normalizado[nombre] = 0

        conteo_normalizado[nombre] += 1

for medicamento, cantidad in conteo_normalizado.items():
    print(medicamento, ":", cantidad)


# ------------------------------------------------
# 5. CONTEO UNIFICADO CON EQUIVALENCIAS
# ------------------------------------------------

print("\n4. CONTEO UNIFICADO")

conteo_unificado = {}

for registro in registros:

    for medicamento in registro["medicamentos"]:

        nombre = medicamento.strip().casefold()

        # Consultar si existe una equivalencia publicada
        nombre_final = equivalencias.get(nombre, nombre)

        if nombre_final not in conteo_unificado:
            conteo_unificado[nombre_final] = 0

        conteo_unificado[nombre_final] += 1

for medicamento, cantidad in conteo_unificado.items():
    print(medicamento, ":", cantidad)


# ------------------------------------------------
# 6. CONTAR PACIENTES DISTINTOS
# ------------------------------------------------

print("\n5. PACIENTES DISTINTOS")

pacientes_distintos = set()

for registro in registros:
    pacientes_distintos.add(registro["paciente_id"])

print("Total de atenciones:", len(registros))
print("Pacientes distintos:", len(pacientes_distintos))


# ------------------------------------------------
# 7. COMPROBACION DE LOS RESULTADOS
# ------------------------------------------------

print("\n6. COMPROBACION")

suma_literal = sum(conteo_literal.values())
suma_normalizado = sum(conteo_normalizado.values())
suma_unificado = sum(conteo_unificado.values())

print("Suma literal:", suma_literal)
print("Suma normalizada:", suma_normalizado)
print("Suma unificada:", suma_unificado)
print("Total de menciones:", total_menciones)

if (
    suma_literal == total_menciones
    and suma_normalizado == total_menciones
    and suma_unificado == total_menciones
):
    print("COMPROBACION CORRECTA")
else:
    print("ERROR: los resultados no coinciden")


# ------------------------------------------------
# 8. RESUMEN FINAL
# ------------------------------------------------

print("\n7. RESUMEN DEL INFORME")

print("Fuente utilizada:", origen)
print("Atenciones recibidas:", len(registros))
print("Pacientes diferentes:", len(pacientes_distintos))
print("Medicamentos literales:", len(conteo_literal))
print("Medicamentos normalizados:", len(conteo_normalizado))
print("Medicamentos unificados:", len(conteo_unificado))
print("Total de menciones:", total_menciones)

print("\nFIN DEL INFORME - SEMANA 8")
