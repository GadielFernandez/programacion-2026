#juego Adivina el número.

import random

# 1. Inicializar variables
numero_secreto = random.randint(1, 20)
intentos = 0

# 2. Iniciar el ciclo de juego
while True:
    # Pedimos el intento al usuario
    intento = int(input("Ingrese un número entero (1-20): "))

    # Contamos los intentos
    intentos += 1

    # Calculamos la distancia
    distancia = abs(numero_secreto - intento)

    # 3. Pistas de dirección
    if numero_secreto < intento:
        print("El número secreto es menor (debes bajar).")
    elif numero_secreto > intento:
        print("El número secreto es mayor (debes subir).")

    # 4. Pistas de temperatura
    if distancia == 0:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif distancia <= 2:
        print("Hirviendo: estás casi encima del número.")
    elif distancia <= 5:
        print("Caliente: estás cerca.")
    elif distancia <= 10:
        print("Tibio: estás cerca, vas por buen camino.")
    else:
        print("Frío: estás lejos.")