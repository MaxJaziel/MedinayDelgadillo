import math

def leer_numero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            return float(texto)
        except:
            print("Escribe un número válido.")

def guardar_historial(texto):
    archivo = open("historial.txt", "a")
    archivo.write(texto + "\n")
    archivo.close()

def cuadrado(l):
    area = l * l
    perimetro = l * 4
    return area, perimetro

def trianguloesc(l1, l2, l3):
    perimetro = l1 + l2 + l3
    s = (l1 + l2 + l3) / 2
    area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))
    return area,perimetro ,s

def trianguloequi(lado):
    perimetro = lado * 3
    area = math.sqrt(3 / 4) * lado ** 2
    return area, perimetro

def trainguloiso(base,altura):
    perimetro = 2 * math.sqrt((base / 2) ** 2 + altura ** 2) + base
    area = (base * altura) / 2
    return area, perimetro

def circulo(radio):
    area = math.pi * radio**2
    perimetro = (radio * 2) * math.pi
    return area ,perimetro 

opcion_historial = ""
print("¿Desea ver el historial previo de operaciones? (s/n)")
opcion_historial = input("> ")

if opcion_historial.lower() == "s":
    try:
        archivo = open("historial.txt", "r")
        contenido = archivo.read()
        archivo.close()
        print("===== HISTORIAL ANTERIOR =====")
        print(contenido)
    except FileNotFoundError:
        print("No existe historial aún.")

opcion = 0
while opcion != 5:
    print("1.Cuadrado")
    print("2.Triangulo")
    print("3.Rectangulo")
    print("4.Circulo")
    print("5.Salir")

    opcion = int(input("Elige una opción ('1', '2', '3', '4', '5'): "))
    a = None
    p = None
    texto = ""

    if opcion == 1:
        l = leer_numero("Ingrese el valor del lado: ")
        a, p = cuadrado(l) 
        texto = f"Area cuadrado: {l} x {l} = {a} \nPerimetro cuadrado :{l} x 4  = {p}"
    elif opcion == 2:
        print("1.Escaleno")
        print("2.Equilatero")
        print("3.Isoceles")
        op = int(input(">"))
        if op == 1:
            l1 = leer_numero("Ingrese el lado #1: ")
            l2 = leer_numero("Ingrese el lado #2: ")
            l3 = leer_numero("Ingrese el lado #3: ")
            a,p,s = trianguloesc(l1,l2,l3)
            texto =f"Area Triangulo Esc. v(({s})({s} - {l1})({s} - {l2})({s} - {l3}) ) = {a}\nPerim. Triangulo Esc. : {l1} + {l2} + {l3} = {p}"
        elif op == 2:
            l = leer_numero("Ingrese el valor del lado: ")
            a, p = trianguloequi(l)
            
            texto = f"Area Triangulo Equilatero: (3 / 4) x {l}² = {a}\nPerimetro Triangulo Equilatero: {l} x 3 = {p}"
        elif op == 3:
            base  = leer_numero("Ingrese el valor de la base:")
            altura = leer_numero("Ingresa el valor de las la altura: ")
            a, p = trainguloiso(base, altura)
            texto = f"Area Triangulo Isoceles: ({base} x {altura}) / 2 = {a}\nPerimetro Triangulo Isoceles: 2 x  v(({base} / 2)² + {altura}²) + {base} = {p}"
    elif opcion == 3:
        base = leer_numero("Ingresa el valor de la base: ")
        altura = leer_numero("Ingresa el valor de la altura: ")
        a, p = trainguloiso(base,altura)
        texto = f"Perimetro Rectangulo: {base} + {base} + {altura} + {altura} = {p}\nArea Rectangulo: {base} x {altura} = {a}"
    elif opcion == 4:
        radio = leer_numero("Ingrese el valor del radio :")
        a, p = circulo(radio)
        texto = f"Area circulo : pi * {radio}**2 = {radio}\nPerimetro : ({radio} * 2) * pi = {p}"

    if a is not None and p is not None:
        print("Resultado del area: ", a)
        print("Resultado del perimetro: ", p)
        guardar_historial(texto)
        print("Operación guardada en historial.txt")