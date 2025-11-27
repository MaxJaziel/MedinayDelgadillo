n = int(input("Ingresa un número: "))

a = 0
b = 1
print("Serie de Fibonacci:")

for i in range(n):
    print(a)
    a, b = b, a + b