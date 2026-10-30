"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300
total_asistentes = 0
bloques_superan_70 = 0

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
for asistencia in asistencias:
    # Acumular el total de asistentes
    total_asistentes += asistencia
    
    # Contar bloques que superan el 70% de la capacidad
    if asistencia > 0.7 * capacidad:
        bloques_superan_70 += 1
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total_asistentes / len(asistencias)
porcentaje_ocupacion = (promedio / capacidad) * 100
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if promedio >= 0.8 * capacidad:
    estado = "alta"
elif promedio >= 0.5 * capacidad:
    estado = "media"
else:
    estado = "baja"
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
print(f"total_asistentes: {total_asistentes}")
print(f"promedio: {promedio}")
print(f"porcentaje_ocupacion: {porcentaje_ocupacion:.0f} %")
print(f"bloques_superan_70: {bloques_superan_70}")
print(f"estado: {estado}")
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
