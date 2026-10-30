"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]
total_precios = sum(precios)
indice = 0
contador_superan_promedio = 0
# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = total_precios / len(precios)
precio_minimo = min(precios)
precio_maximo = max(precios)
rango = precio_maximo - precio_minimo
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
while indice < len(precios):
    if precios[indice] > promedio:
        contador_superan_promedio += 1
    indice += 1

# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    variacion = "alta"
elif rango >= 150:
    variacion = "moderada"
else:
    variacion = "baja"
# TODO: Muestre producto y todos los resultados.
print(f"producto: {producto}")
print(f"promedio: {promedio}")
print(f"precio_minimo: {precio_minimo}")
print(f"precio_maximo: {precio_maximo}")
print(f"rango: {rango}")
print(f"contador_superan_promedio: {contador_superan_promedio}")
print(f"variacion: {variacion}")
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
