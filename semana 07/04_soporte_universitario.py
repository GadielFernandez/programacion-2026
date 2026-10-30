"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
acumulador_minutos = 0
conteo_categoria = {"Acceso": 0, "Equipo": 0, "Red": 0}
contador_pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
minutos_atencion_max = ()

# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
for incidencia in incidencias:
    acumulador_minutos += incidencia["minutos_atencion"]
    categoria = incidencia["categoria"]
    if categoria in conteo_categoria:
        conteo_categoria[categoria] += 1
    else:
        conteo_categoria[categoria] = 1

# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
    minutos = incidencia["minutos_atencion"]
   
    if not minutos_atencion_max or minutos > minutos_atencion_max[1]:
       minutos_atencion_max = (incidencia["id"], minutos)
       
    if not incidencia["resuelto"]:
        contador_pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])
        if minutos >= 60:
            casos_urgentes.append((incidencia["id"], minutos)) 
# TODO: 
promedio_minutos = acumulador_minutos / len(incidencias)

print(f"Total de minutos: {acumulador_minutos}")
print(f"Promedio de minutos: {promedio_minutos:.2f}")
print(f"Conteo por categoría: {conteo_categoria}")
print(f"Casos pendientes: {contador_pendientes}")
print(f"Provincias con pendientes: {provincias_pendientes}")
print(f"Casos urgentes: {casos_urgentes}")
print(f"Caso con más minutos de atención: {minutos_atencion_max}")
print(f"hay pendientes en San Jose? {'San Jose' in provincias_pendientes}")
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.