import math
def guardar_historial(texto):
    archivo = open("historial.txt", "a")
    archivo.write(texto + "\n")
    archivo.close()


def cuadrado(l): 
    return l * l

def p_triangulo_escaleno(l1,l2,l3):
    return l1 + l2 + l3
def a_triangulo_escaleno()
     math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3)) )


opcion = ""
while opcion != "5":
    print("1.Cuadrado")
    print("2. Triangulo")
    print("3. Rectangulo")
    print("4. Circulo")

    opcion = input("Elige una opción ('1', '2', '3', '4', '5'): ")