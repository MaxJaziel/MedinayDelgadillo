contador = 0
cont_impar = 0
n = int(input("¿Cuantos numeros se van a ingresar: "))
for i in range (1,n + 1):
    num = int(input(f"Ingrese el valor {i}: "))
    if num % 2 == 0: 
        contador = contador + 1
    else: 
        cont_impar = cont_impar + 1
print(f"Hay {contador} numero pares y {cont_impar} numeros impares")