
# Diagnóstico semanal de ventas
# Comparación de las tiendas Centro y Norte

# 1. Datos de las tiendas
ventas_centro = [125000, 98000, 147000, 132000, 110000]
meta_centro = 640000

ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_norte = 700000

# 2. Cálculos de la tienda Centro
total_centro = sum(ventas_centro)
dias_centro = len(ventas_centro)
promedio_centro = total_centro / dias_centro
mayor_centro = max(ventas_centro)
menor_centro = min(ventas_centro)
rango_centro = mayor_centro - menor_centro

diferencia_centro = total_centro - meta_centro
porcentaje_centro = (total_centro / meta_centro) * 100

if total_centro > meta_centro:
    estado_centro = "Meta superada"
elif total_centro == meta_centro:
    estado_centro = "Meta alcanzada exactamente"
else:
    estado_centro = "Meta no alcanzada"

# 3. Cálculos de la tienda Norte
total_norte = sum(ventas_norte)
dias_norte = len(ventas_norte)
promedio_norte = total_norte / dias_norte
mayor_norte = max(ventas_norte)
menor_norte = min(ventas_norte)
rango_norte = mayor_norte - menor_norte

diferencia_norte = total_norte - meta_norte
porcentaje_norte = (total_norte / meta_norte) * 100

if total_norte > meta_norte:
    estado_norte = "Meta superada"
elif total_norte == meta_norte:
    estado_norte = "Meta alcanzada exactamente"
else:
    estado_norte = "Meta no alcanzada"
    
#Resultados tienda_centro
    
    