def agregar_estudiantes(lista):
    nombre = input("ingrese el nombre del estudiantes: ").strip().upper()
    lista.append(nombre)
    
    return lista
    

estudiantes = ["Gadiel", "Andres", "Juan", "María"]

while True:
    opcion = input("opciones 1.Agregar estudiantes. 2.listar estudiantes, 3.salir")
    if opcion == "1":
        estudiantes = agregar_estudiantes(estudiantes)
        print("estudiante agregado exitosamente")
    elif opcion == "2":
        for estudiante in estudiantes:
            print(estudiante)
    elif opcion == "3":
        break
    else:
        print("opcion invalida")