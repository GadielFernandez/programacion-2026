from sedes import emprendimientos

print("Emprendimientos registrados:", len(emprendimientos))
print("Primer emprendimiento:", emprendimientos[0]["nombre"])
print("Primer emprendimiento ventas:", emprendimientos[0]["ventas"])



#Cada vuelta procesara un diccionario
for empre in emprendimientos:
    total = sum(empre['ventas'])
    porcentaje = total / empre['meta'] * 100
    
    
    
    if porcentaje >= 100:
        estado = "Meta alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atención!"
        
    print(
        f"{empre["nombre"]} | Total: ₡{total:,.2f} | "
        f"Cumplimiento: {porcentaje:.2f}% | {estado}"
    )