contraseña = 12345
contador = 0
while contador < 5 :
    contra = int(input("Ingresa la contraseña:\n"))
    if contra != contraseña:
        contador = contador + 1
    elif contra == contraseña:
        print("Contraseña correcta")
        contador = 6      
    if contador >= 5:
        print("Te quedaste sin intentos")
        contador = 5
