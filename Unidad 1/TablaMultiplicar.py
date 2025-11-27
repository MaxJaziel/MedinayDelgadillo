print("Tabla de multiplicar: ")
numero= int(input("Introduce un numero: "))
print(f"\n Tabla del {numero} :" )
for i in range  (1,11):
    resultado = numero * i 
    print(f"{numero}x{i}={resultado}")