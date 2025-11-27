#Hecho por Medina Morelos y Delgadillo Garcia
print("1.suma" )
print("2.resta" )
print("3.multiplicacion" )
print("4.division" )
n= float(input("¿Que desea usar?"))
if n==1:
    a=float(input("Primer Numero:"))
    b=float(input("Segundo numero:"))
    r=a + b
    print("El resultado es:" , r)

elif n==2:
    a=float(input("Primer Numero:"))
    b=float(input("Segundo numero:"))
    r=a - b
    print("El resultado es:" , r)

elif n==3:
    a=float(input("Primer Numero:"))
    b=float(input("Segundo numero:"))
    r=a*b
    print("El resultado es:" , r)


elif n == 4:
    a = float(input("Primer Numero: "))
    b = float(input("Segundo numero: "))

    if b == 0:
        print("Error: No se puede dividir ")
    elif a == 0:
        print("Error: No se puede dividir ")
    else:
        r = a / b
        print("El resultado es:", r)