n = int(input("Ingresa un numero: "))

factorial = 1
for i in range(1, n+1):
    factorial *= i

print("EL resultado es " , factorial )