numeros =[]
multiplos = []
mayor = 0 
mayorn = 0

for i in  range(1,8):
    n =int(input(f"Ingresa el numero #{i}: "))
    numeros.append(n)
    multiplo = n % 3 
    if multiplo == 0:
        multiplos.append(n)
    if n > mayor:
        mayor  = n 
        posicion = i
promedio = sum(numeros) / 7
print(f"\nEl promedio es : {promedio}")
print(f"Multiplos de 3: {multiplos}")
numeros.pop(posicion - 1)
for numero in numeros:
    if numero > mayorn:
        mayorn = numero
print(f"El segundo mayor es: {mayorn}")
