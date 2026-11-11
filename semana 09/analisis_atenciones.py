"""
Expediente de 12 atenciones ficticias.

Complete lector_csv.py y siga la guía de Semana 09. Cambie ETAPA de 1 a 2
y luego a 3 conforme verifique cada parte con python analisis_atenciones.py.
"""

from lector_csv import cargar_atenciones


ETAPA = 1


def explorar_atenciones(atenciones):
    """Recibe la lista de atenciones y muestra el total, los tipos y los campos."""
    # P1. Complete el lector y compruebe el mensaje de archivo faltante.
    if not atenciones:
        print("Revise los TODO de lector_csv.py antes de continuar.")
    else:
        print("P1. Archivo leído correctamente.")

    # P2. Cuente las filas con un ciclo. Compruebe que obtuvo 12.
    total = 0
    for atencion in atenciones:
        total += 1
    print(f"Total de atenciones contadas: {total}")

    # P3. Ejemplo listo para ejecutar. Explique qué tipos y campos observa.
    primer_registro = atenciones[0]
    print(f"Primer registro: {primer_registro}")
    print(f"Tipo de primer registro: {type(primer_registro)}")
    print("Campos del registro y el tipo de cada valor:")
    for campo in primer_registro:
        print(f"  {campo}: {type(primer_registro[campo])}")


def contar_y_limpiar(atenciones):
    """Recibe la lista de atenciones y muestra los conteos y sus comprobaciones."""
    print("Etapa 2. Complete y compruebe las preguntas 4 a 8.")

    # P4. Cuente los medicamentos tal como aparecen en el CSV con .get().
    # Muestre el contador y su total.
    contador_medicamentos = {}

    # TODO: Completar P4.

    # P5. Muestre ejemplos de espacios o mayúsculas en hospital,
    # diagnostico y medicamento.
    print("P5. Ejemplos de espacios o mayúsculas:")

    # TODO: Completar P5.

    # P6. Cuente los medicamentos con strip() y lower(). Muestre el
    # contador limpio y su total. Compare con P4.

    # TODO: Completar P6.

    # P7. Agrupe los nombres limpios con las equivalencias de la guía.
    # Complete el diccionario. La clave es la variante y el valor es
    # el nombre que conservará. El nuevo contador debe sumar 12.
    equivalencias = {
        # TODO: Completar las equivalencias.
    }

    # TODO: Completar P7.

    # P8. Cuente hospitales y diagnósticos con los nombres limpios.
    # Muestre ambos contadores, sus totales y la categoría más frecuente
    # de cada campo.

    # TODO: Completar P8.


def concluir(atenciones):
    """Recibe la lista de atenciones y muestra el resumen de pacientes y esperas."""
    print("Etapa 3. Complete y compruebe las preguntas 9 y 10.")

    # P9. Cuente por cédula. Muestre cuántas personas hay, cuáles cédulas
    # se repiten y si coinciden el nombre, la edad y la provincia.

    # TODO: Completar P9.

    # P10. Sume minutos_espera con un ciclo. Muestre el total y el promedio.
    # Redacte un hallazgo que use el promedio y un conteo.

    # TODO: Completar P10.


atenciones = cargar_atenciones()

if not atenciones:
    print("Revise los TODO de lector_csv.py antes de continuar.")
elif ETAPA == 1:
    explorar_atenciones(atenciones)
elif ETAPA == 2:
    contar_y_limpiar(atenciones)
elif ETAPA == 3:
    concluir(atenciones)
else:
    print("Seleccione 1, 2 o 3 en ETAPA.")
