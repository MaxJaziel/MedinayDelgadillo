personas = [{"nombre" : "max" , "edad" : 17 , "ciudad" : "tampico"},
            {"nombre" : "david" , "edad" : 16 , "ciudad" : "madero"},
            {"nombre" : "julian" , "edad" : 80 , "ciudad" : "altamira"},
            {"nombre" : "jose" , "edad" : 20 , "ciudad" : "tampico"},
            {"nombre" : "fernanda" , "edad" : 56 , "ciudad" : "madero"},
            {"nombre" : "kevin" , "edad" : 28 , "ciudad" : "madero"},
            {"nombre" : "jaime" , "edad" : 45 , "ciudad" : "altamira"},
            {"nombre" : "areli" , "edad" : 7 , "ciudad" : "madero"},
            {"nombre" : "eidan" , "edad" : 19 , "ciudad" : "tampico"},
            {"nombre" : "luis" , "edad" : 78 , "ciudad" : "tampico"}
            ]
opcion = 0 
mayores = []
menores = []
adultosmayores = []
ciudadimprimir = []
while opcion != 5:
    print("1.Agregar persona")
    print("2.Modificar persona")
    print("3.ELiminar persona")
    print("4.Imprimir")
    print("5.Salir")
    opcion = int(input("ELija una opcion :"))
    if opcion == 1:
        nombreagg = input("Ingrese el nombre de la persona que desea agregar: ")
        edadagg = input("Ingresa la edad de la persona: ")
        ciudadagg = input("Ingresa la ciudad: ")
        personagg = {"nombre" : nombreagg , "edad" : edadagg , "ciudad" : ciudadagg }
        personas.append(personagg)
        print(personas)
    elif opcion == 2:
        nombremod = input("Ingrese el nombre de la persona a modificar: ")
        for persona in personas: 
            if persona["nombre"] == nombremod:
                salirmod = 0 
                while salirmod != 4:
                    print("¿Que desea modificar?")
                    print("1.Cambiar nombre")
                    print("2.Cambiar edad ")
                    print("3.Cambiar ciudad")
                    print("4.Salir")
                    opmod = int(input(""))
                    if opmod == 1:          
                        nuevonombre = input("Ingrese el nuevo nombre: ")
                        persona["nombre"] = nuevonombre
                        print(personas)
                    elif opmod == 2:
                        nuevaedad = int(input("Ingrese la nueva edad: "))
                        persona["edad"] = nuevaedad
                        print(personas)
                    elif opmod == 3:
                        nuevaciudad = input("Ingresa la nueva ciudad")
                        persona["ciudad"] = nuevaciudad
                        print(personas)
                    elif opmod == 4:
                        salirmod = 4
                        print("/n")
    elif opcion == 3:
        nombre = input("Ingrese el nombre de la persona que quiere eliminar")
        for persona in personas :
            if persona["nombre"] == nombre:
                personas.remove(persona)
                print("Eliminado con exito \n")
                print(personas)
    elif opcion == 4:
        print("1.Imprimir por edad")
        print("2.imprimir por ciudad")
        print("3.Imprimir todos")
        op = int(input(" "))
        if op == 1: 
            for persona in personas:
                if persona["edad"] < 18:
                    menores.append(persona)
                elif persona["edad"] > 18:
                    mayores.append(persona)
                elif persona["edad"] > 75:
                    adultosmayores.append(persona)
            print("1.mayores")
            print("2.menores")
            print("3.adultos mayores")
            opc = int(input(""))
            if opc == 1:
                archivo = open("demo.txt" , "w")
                for persona in mayores:
                    archivo.write(f"{persona}\n")
                archivo.close()
            elif opc == 2:
                archivo = open("demo.txt" , "w")
                for persona in menores:
                    archivo.write(f"{persona}\n")
                archivo.close()
            elif opc == 3:
                archivo  = open("demo.txt", "w")
                for persona in adultosmayores:
                    archivo.write(f"{persona}\n")
        elif op == 2:
            ciudadimp = input("Ingresa la ciudad: ")
            for persona in personas:
                    if persona["ciudad"] == ciudadimp:
                            ciudadimprimir.append(persona)
                    archivo = open("demo.txt" , "w")
                    for persona in ciudadimprimir: 
                        archivo.write(f"{persona}\n")
                    archivo.close()
            print("Se ha creado el archivo con exito\n")
        elif op == 3:
            archivo = open("demo.txt" , "w")
            for persona in personas:
                archivo.write(f"{persona}\n")
            archivo.close()
            print("Se ha creado con exito el archivo\n")
    elif opcion == 5:
        opcion = 5
    else:
        opcion = 5