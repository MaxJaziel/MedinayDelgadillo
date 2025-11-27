
contador = 0
import random
numero_secreto = random.randint (1,20)
adivinado = False
while adivinado == False:
    numero = int(input("Introduce un numero entre 1 y 20:\n"))
    if numero != numero_secreto:
        contador = contador + 1
    if numero < numero_secreto:
        print("El  numero es mayor")
    elif numero > numero_secreto:
        print("El numero es menor")
    elif numero == numero_secreto:
        print(f"El numero correcto es {numero_secreto}")
        print(f"Contador de intentos:{contador}")
        adivinado = True



