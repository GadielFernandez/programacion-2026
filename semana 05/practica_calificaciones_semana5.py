#Lista de notas
calificaciones = [65.84, 98.23, 85.25]

#Reemplazar nota
calificaciones[1] = 70

#Añadir notas
calificaciones_2 = [96, 100]

#Concatenar notas
calificaciones_2 = calificaciones + calificaciones_2
print("calificaciones:", calificaciones_2)
calificaciones.sort()

#ingresar nuvea calificación
nueva_calificación = float(input("ingrese calificación: "))
calificaciones.append(nueva_calificación)

#Obtener max(),min(),len()
calificacion_mayor = max(calificaciones)
print("calificación mayor:", calificacion_mayor)
calificacion_menor = min(calificaciones)
print("calificación menor:", calificacion_menor)
cantidad_calificaciones = len(calificaciones)
print("cantidad de calificaciones:", cantidad_calificaciones)

#Agreagr nueva calificación
calificaciones.insert(1, 88)
#Eliminar calificación
calificaciones.remove(85.25)

if 100 in calificaciones:
    print("si está nota buscada")
else:
    print("no se encuentra nota")