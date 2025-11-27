usuario1 = "ana"
contraseña1 = "123"
usuario2 = "luis"
contraseña2 = "ABC"
usuario3 = "pedro"
contraseña3 = "192"
intentos = 0
while intentos < 3:
    usuario = input("Ingrese el usuario :")
    if usuario == usuario1 or usuario == usuario2 or usuario == usuario3:
        contraseña = input("Ingresa la contraseña: ")
        if contraseña == contraseña1 or contraseña == contraseña2 or contraseña == contraseña3:
            print("Acceso autorizado")
            intentos = 4
        elif contraseña != contraseña1 and contraseña != contraseña2 and contraseña != contraseña3:
            print("contraseña no valida")
            intentos =+ 1
    else :
        print("Usuario no valido: ")
        intentos =+ 1