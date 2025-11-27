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

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("No se puede dividir entre cero.")
        return None
    return a / b

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

opcion = ""
while opcion != "5":
    print("\n====== CALCULADORA ======")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

    opcion = input("Elige una opción ('1', '2', '3', '4', '5'): ")

    if opcion in ("1", "2", "3", "4"):
        num1 = leer_numero("Número 1: ")
        num2 = leer_numero("Número 2: ")
        resultado = None
        texto = ""

        if opcion == "1":
            resultado = sumar(num1, num2)
            texto = f"{num1} + {num2} = {resultado}"
        elif opcion == "2":
            resultado = restar(num1, num2)
            texto = f"{num1} - {num2} = {resultado}"
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            texto = f"{num1} * {num2} = {resultado}"
        elif opcion == "4":
            resultado = dividir(num1, num2)
            
            if resultado is not None:
                texto = f"{num1} / {num2} = {resultado}"
        
        if resultado is not None:
            print(f"Resultado: {resultado}")
            
            guardar_historial(texto)
            print("Operación guardada en historial.txt")

    elif opcion == "5":
        print("Saliendo...")
    else:
        print("Opción no válida. Intenta de nuevo.")