import math
print("1.Cuadrado")
print("2. Triangulo")
print("3. Rectangulo")
print("4. Circulo")
opcion  = int(input("Elige  una opcion: "))
match opcion :
    case 1 :
        lado = float(input("introduce el valor del lado"))
        print("Perimetro es igual a:", lado * 4)
        print("Area es igual a", lado * lado)
    case 2:
        print("2.1 Escaleno")
        print("2.2 Equilatero")
        print("2.3 Isoceles")
        op = float(input("Elija una opcion (2.1-2.3): "))
        match op:
            case 2.1:
                lado1 = float(input("Introduce el valor del lado"))
                lado2 = float(input("Introduce el valor del lado"))
                lado3 = float(input("Introduce el valor del lado"))
                print("Perimetro es igual a:", lado1 + lado2 + lado3)
                s = (lado1 + lado2 + lado3) / 2
                print("Area es igual a:", math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3)) )
            case 2.2:
                lado = float(input("introduce el valor del lado"))
                print("Perimetro es igual a", lado * 3)
                print("Area es igual a", math.sqrt(3 / 4) * lado ** 2)
            case 2.3: 
                lado = float(input("Introduce elvalor del lado:"))
                base = float(input("Introduce elvalor de la base:" ))
                p = 2* lado + base 
                h = math.sqrt(lado**2 - (base/2)**2)
                a = (lado * h / 2)
                print ("El perimetro es: " , p)
                print ("El area es igual a: " , a)
    case 3:
        base= float(input("Ingresa el valor de la base: "))
        altura = float(input("Ingresa el valor de la altura: "))
        p = 2 * altura + 2* base 
        a = base * altura 
        print("El perimetro es : ", p)
        print("El area es : ",a)
    case 4: 
        radio=float(input("Ingresa el radio:"))
        pi = math.pi
        area = pi * radio**2
        p = 2 * math.pi * radio
        print("El perimetro es" , p )
        print("El area es" , area )