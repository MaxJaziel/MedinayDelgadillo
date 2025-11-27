def saludar():
	print("Llamando a la funcion: saluda()")
saludar()
print("\nComentario:")
print("-'def' sirve para definir funciones")
print("-No recibe datos entre parentesis(No tiene parametros")
print("-Solo se ejecuta cuando la llamas por su nombre")

def saludar_nombre(nombre):
	print("Hola", nombre)
saludar_nombre("Ana")
print ("\nAhora escribe tu nombre: ")
tu_nombre = input("Nombre: ")
print ("Llamando a la funcion con tu nombre: ")
saludar_nombre(tu_nombre)

print("\nComentarios")
print("-'Nombre'es un parametro")
print("-El valor que le mandamos (por ejemplo 'Ana') ")

def cuadrado(n):
	return n * n

print("Ejemplo: resultado = cuadrado(5)")
resultado = cuadrado(5)
print("El valor del resultado es:" , resultado)

print("\nAhora escribe un numero y te doy su cuadrado: ")
num =  int(input("Numero: "))
print("cuadrado(",num,") es : ", cuadrado(num))

def sumar(a,b):
	return a + b
def restar(a,b):
	return a - b
opcion = ""
print("Menu de la calculadora: " )
print("1)Sumar")
print("2)Restar")
a = float(input("Numero 1: "))
b = float(input("Numero 2: "))
opcion = input("Elige una opcion: ")
if opcion == "1":
	r = sumar(a,b)
	print("Resultado de la suma: ", r)
elif opcion == "2":
	r = restar(a,b)
	print("Resultado  de la resta: " , r)
else:
	print("Opcion no valida")
