secreto = 7
intentos = 1
max_intentos = 5
adivina_numero = int(input("ingrese un numero entero (0, 10): "))

while adivina_numero != secreto and intentos < max_intentos:
    if adivina_numero < 0 or adivina_numero > 10:
        print(" el numero ingresado no es valido, ingrese un numero entre 0 y 10")
    elif adivina_numero > secreto:
        print("El numero secreto es menor") 
    else:
        print("El numero secreto es mayor")
        
   
    adivina_numero = int(input("ingrese un numero entero: (0, 10)"))
    intentos += 1
    
if adivina_numero == secreto:
    print("¡felicidades, adivinaste el numero!")
    print(f"Numero de intentos: {intentos}")
else:
    print("Lo siento, no adivinaste el numero secreto")
    print(f"intentos maximos: {max_intentos}")
    print(f"El numero secreto era: {secreto}")
    


   
   
    
    