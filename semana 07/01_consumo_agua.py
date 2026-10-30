"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
consumo_total = sum(consumos_litros)
promedio_diario = consumo_total / len(consumos_litros)
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
dia_primero = consumos_litros[0]
dia_ultimo = consumos_litros[-1]
litros_ahorrados = dia_primero - dia_ultimo
porcentaje_reduccion = (litros_ahorrados / dia_primero) * 100
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if porcentaje_reduccion >= 15:
    clasificacion = "Reducción alta"
elif porcentaje_reduccion > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"
# TODO: Muestre los cinco resultados.
print("control: total", consumo_total)
print("control: promedio", promedio_diario)
print("control: ahorro", litros_ahorrados)
print("control: reducción", porcentaje_reduccion)
print("control: clasificación", clasificacion)
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
