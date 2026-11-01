# Microreto: Analisis de ventas de Cafe

# Lista con los datos del producto
producto = ["Cafe", 5000, 20]

# Porcentaje de aumento esperado en las ventas
porcentaje_aumento = 20

# Calcular el descuento del 15 %
descuento = producto[1] * 15 / 100

# Calcular el precio promocional
precio_promocional = producto[1] - descuento

# Calcular el ingreso actual
ingreso_actual = producto[1] * producto[2]

# Calcular el aumento de unidades vendidas
aumento_unidades = producto[2] * porcentaje_aumento / 100

# Calcular las unidades proyectadas
unidades_proyectadas = producto[2] + aumento_unidades

# Calcular el ingreso proyectado
ingreso_proyectado = precio_promocional * unidades_proyectadas

# Calcular la diferencia entre los ingresos
diferencia = ingreso_proyectado - ingreso_actual

# Mostrar los resultados
print(f"Producto: {producto[0]}")
print(f"Precio actual: ₡{producto[1]:.2f}")
print(f"Unidades vendidas: {producto[2]}")
print(f"Descuento del 15 %: ₡{descuento:.2f}")
print(f"Precio promocional: ₡{precio_promocional:.2f}")
print(f"Ingreso actual: ₡{ingreso_actual:.2f}")
print(f"Porcentaje de aumento: {porcentaje_aumento}%")
print(f"Aumento de unidades: {aumento_unidades:.2f}")
print(f"Unidades proyectadas: {unidades_proyectadas:.2f}")
print(f"Ingreso proyectado: ₡{ingreso_proyectado:.2f}")
print(f"Diferencia de ingresos: ₡{diferencia:.2f}")

# Tomar la decision
if diferencia > 0:
    print("Recomendacion: lanzar")
else:
    print("Recomendacion: no lanzar")