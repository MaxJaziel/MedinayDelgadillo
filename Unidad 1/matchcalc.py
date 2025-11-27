print("1.suma" )
print("2.resta" )
print("3.multiplicacion" )
print("4.division" )
n= float(input("¿Que desea usar?"))
match n:
        case 1:
            a=float(input("Primer Numero:"))
            b=float(input("Segundo numero:"))
            r=a + b
            print("El resultado es:" , r)
        case 2:
            a=float(input("Primer Numero:"))
            b=float(input("Segundo numero:"))
            r=a - b
            print("El resultado es:" , r)
        case 3:
            a=float(input("Primer Numero:"))
            b=float(input("Segundo numero:"))
            r=a*b
            print("El resultado es:" , r)
        case 4:
            a = float(input("Primer Numero: "))
            b = float(input("Segundo numero: "))
            match a:
                case 0:
                    print("Error: No se puede dividir")
                case _ :
                    r = a / b
                    print("El resultado es:", r)