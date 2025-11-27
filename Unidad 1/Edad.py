nombre = input(("¿Cual es tu Nombre? "))
edad = float(input("¿Cual es tu edad? "))
if edad <18:
    print("No puedes votar,eres menor de edad")
elif edad >=18: 
    print("Eres mayor de edad")
    if edad >=75:
        print("Tienes voto preferencial,no haces fila")
    elif edad > 18 and edad <75:
        print("Puedes votar")




