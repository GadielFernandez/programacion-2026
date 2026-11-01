capacidad = 700
grupos_aceptados = []
grupos_rechazados = []
ocupacion = 0

entrada = input(
    "Ingrese la cantidad de personas del grupo o 'fin' para terminar: "
).strip().lower()

while entrada != "fin":
    try:
        grupo = int(entrada)

        if grupo <= 0:
            print("Entrada inválida: ingrese un entero mayor que cero.")
        else:
            if ocupacion + grupo <= capacidad:
                grupos_aceptados.append(grupo)
                ocupacion += grupo
                print(f"Grupo aceptado: ingresan {grupo} personas.")
            else:
                grupos_rechazados.append(grupo)
                print(
                    f"Grupo rechazado: no hay espacio para {grupo} personas."
                )

            print(f"Ocupación actual: {ocupacion}")
            print(f"Espacios disponibles: {capacidad - ocupacion}")

    except ValueError:
        print("Entrada inválida: debe ingresar un número entero o 'fin'.")

    entrada = input(
        "Ingrese la cantidad de personas del grupo o 'fin' para terminar: "
    ).strip().lower()

print("\nREPORTE FINAL")

print(f"Grupos aceptados: {len(grupos_aceptados)}")
print(f"Grupos rechazados: {len(grupos_rechazados)}")
print(f"Personas admitidas: {ocupacion}")
print(f"Capacidad máxima: {capacidad}")
print(f"Espacios disponibles: {capacidad - ocupacion}")

porcentaje = ocupacion / capacidad * 100
print(f"Porcentaje de ocupación: {porcentaje:.2f}%")

if len(grupos_aceptados) > 0:
    menor = grupos_aceptados[0]
    mayor = grupos_aceptados[0]

    for grupo in grupos_aceptados:
        if grupo < menor:
            menor = grupo
        if grupo > mayor:
            mayor = grupo

    print(f"Grupo aceptado más pequeño: {menor}")
    print(f"Grupo aceptado más grande: {mayor}")
else:
    print("No hubo grupos aceptados.")

if ocupacion < 560:
    print("Estado final: disponibilidad normal.")
elif ocupacion < 700:
    print("Estado final: ocupación preventiva.")
else:
    print("Estado final: capacidad completa.")


