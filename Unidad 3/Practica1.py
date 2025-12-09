def leer_numero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            return float(texto)
        except:
            print("Ingresa un numero valido")

n = leer_numero("Ingresa un numero")
print(n)
