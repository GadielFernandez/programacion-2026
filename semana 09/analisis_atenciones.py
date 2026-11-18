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
"""""primer_registro = atenciones[0] toma el primer elemento de la lista (indice 0) es el diccionario de Ana Morales.
print(f"Primer registro: {primer_registro}") muestra el tipo de dato del registro. type() le dice que es el objeto.
campos del registro y el tipo de cada valor: recorre cada campo del diccionario y muestra el nombre del campo y el tipo de dato de su valor."""

def contar_y_limpiar(atenciones):
    """Recibe la lista de atenciones y muestra los conteos y sus comprobaciones."""
    print("Etapa 2. Complete y compruebe las preguntas 4 a 8.")

    # P4. Cuente los medicamentos tal como aparecen en el CSV con .get().
    # Muestre el contador y su total.
    
   
    contador_medicamentos = {}
    for atencion in atenciones:
        medicamento = atencion["medicamento"]
        contador_medicamentos[medicamento] = contador_medicamentos.get(medicamento, 0) + 1
    print("P4. Conteo de medicamentos tal como aparecen en el CSV:")
    for medicamento, cantidad in contador_medicamentos.items():
        print(f"{medicamento}: {cantidad}")
    total_medicamentos = sum(contador_medicamentos.values())
    print(f"Total de medicamentos contados: {total_medicamentos}")

    # TODO: Completar P4.

    # P5. Muestre ejemplos de espacios o mayúsculas en hospital,
    # diagnostico y medicamento.
    for campo in ["hospital", "diagnostico", "medicamento"]:
        valores = [atencion[campo] for atencion in atenciones]
        valores_unicos = set(valores)
        print(f"\nEjemplos de '{campo}' con espacios o mayúsculas:")
        for valor in valores_unicos:
            if valor != valor.strip() or valor != valor.lower():
                print(f"  '{valor}'")
                
    print("P5. Ejemplos de espacios o mayúsculas:")
    

    # TODO: Completar P5.

    # P6. Cuente los medicamentos con strip() y lower(). Muestre el
    # contador limpio y su total. Compare con P4.
    contador_medicamentos_limpio = {}
    for atencion in atenciones:
        medicamento = atencion["medicamento"].strip().lower()
        contador_medicamentos_limpio[medicamento] = contador_medicamentos_limpio.get(medicamento, 0) + 1
    print("\nP6. Conteo de medicamentos limpio (strip() y lower()):")
    for medicamento, cantidad in contador_medicamentos_limpio.items():
        print(f"{medicamento}: {cantidad}")
    total_medicamentos_limpio = sum(contador_medicamentos_limpio.values())
    print(f"Total de medicamentos contados (limpio): {total_medicamentos_limpio}")

    # TODO: Completar P6.

    # P7. Agrupe los nombres limpios con las equivalencias de la guía.
    # Complete el diccionario. La clave es la variante y el valor es
    # el nombre que conservará. El nuevo contador debe sumar 12.
    equivalencias = {
        "losartan": "losartán",
        "acetaminofen": "paracetamol",
        "omeprasol": "omeprazol",
        "Omeprasol": "omeprazol",
        "Meformina": "metformina",
        "meformina": "metformina",
        "Salbutamol": "salbutamol",
        "nitrofurantoina": "nitrofurantoína"     # Ejemplo de equivalencia        # TODO: Completar las equivalencias.
}
    
    # TODO: Completar P7.

    # P8. Cuente hospitales y diagnósticos con los nombres limpios.
    # Muestre ambos contadores, sus totales y la categoría más frecuente
    # de cada campo.
    total_hospitales = {}
    total_diagnosticos = {}
    for atencion in atenciones:
        hospital = atencion["hospital"].strip().lower()
        diagnostico = atencion["diagnostico"].strip().lower()
        total_hospitales[hospital] = total_hospitales.get(hospital, 0) + 1
        total_diagnosticos[diagnostico] = total_diagnosticos.get(diagnostico, 0) + 1
    print(f"\nConteo de hospitales y diagnósticos limpios:")
    print("Hospitales:")
    for hospital, cantidad in total_hospitales.items():
        print(f"{hospital}: {cantidad}")
    print("Diagnósticos:")
    for diagnostico, cantidad in total_diagnosticos.items():
        print(f"{diagnostico}: {cantidad}")
    

    # TODO: Completar P8.


def concluir(atenciones):
    """Recibe la lista de atenciones y muestra el resumen de pacientes y esperas."""
    print("Etapa 3. Complete y compruebe las preguntas 9 y 10.")

    # P9. Cuente por cédula. Muestre cuántas personas hay, cuáles cédulas
    # se repiten y si coinciden el nombre, la edad y la provincia.
    total_por_cedula = {}

    for atencion in atenciones:
        cedula = atencion["cedula"]
        
        if cedula not in total_por_cedula:
            total_por_cedula[cedula] = {
                "nombre": atencion["nombre_paciente"],
                "edad": atencion["edad"],
                "provincia": atencion["provincia"],
                "conteo": 1,
                "coincide": True,
            }
        else:
            registro = total_por_cedula[cedula]
            registro["conteo"] += 1
            if (registro["nombre"] != atencion["nombre_paciente"] or
                registro["edad"] != atencion["edad"] or
                registro["provincia"] != atencion["provincia"]
            ):
                registro["coincide"] = False
                
    print(f"P9. personas distintas: {len(total_por_cedula)}")
    print("Cédulas repetidas")
    for cedula, datos in total_por_cedula.items():
        if datos["conteo"] > 1:
            estado = "sí coinciden" if datos["coincide"] else "no coinciden"
            print(f"Cédula: {cedula} - {datos['nombre']}: - {datos['conteo']} - atenciones "
                f"({estado} nombre, edad y provincia)")
            
    # P10. Sume minutos_espera con un ciclo. Muestre el total y el promedio.
    # Redacte un hallazgo que use el promedio y un conteo.

    # TODO: Completar P10.
    total_minutos = 0
    for atencion in atenciones:
        total_minutos += atencion["minutos_espera"]
        
    promedio = total_minutos / len(atenciones) 

    
    print(f"\ntotal de minutos: {total_minutos}")
    print(f"El promedio de espera es de: {promedio:.1f} minutos")
    
        


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
