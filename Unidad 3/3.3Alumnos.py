opcion = 0 
while opcion != 7:
    print("\n1.Leer archivo")
    print("2.Mostrar lista de alumnos")
    print("3.Agregar alumnos")
    print("4.Modifiar alumnos")
    print("5.Eliminar alumno")
    print("6.Imprimir")
    print("7.Salir")
    opcion = int(input("Elija una opcion: "))
    if opcion == 1: 
        archivo =open("Alumnos.txt" , "r")
        lineas = archivo.readlines()
        for linea in lineas:
            linea = linea.strip()
            partes = linea.split(" ")
            print(partes)
    elif opcion == 2:
        op = 0
        print("1.Completa")
        print("2.Por grado")
        print("3.Por grupo")
        print("4.Por turno")
        print("5.Aprobados o reprobados")
        op = int(input("ELija una opcion: "))
        if op == 1:
            archivo =open("Alumnos.txt" , "r")
            lineas = archivo.readlines()
            archivo.close()
            for linea in lineas:
                linea = linea.strip()
                partes = linea.split(" ")
                print(partes)
        elif op == 2:
            grado = input("¿Que grado desea mostrar?: ")
            archivo =open("Alumnos.txt" , "r")
            lineas = archivo.readlines()
            archivo.close()
            for linea in lineas:
                linea = linea.strip()
                partes = linea.split(" ")
                if partes[2] == grado:
                    print(partes)
        elif op ==3:
            grupo = input("¿Que grupo desea mostrar?")
            archivo =open("Alumnos.txt" , "r")
            lineas = archivo.readlines()
            archivo.close()
            for linea in lineas:
                linea = linea.strip()
                partes = linea.split(" ")
                if partes[3] == grupo:
                    print(partes)
        elif op == 4:
            print("a)Matutino")
            print("b)Vespertino")
            opturno = input("¿Que turno desea mostrar?")
            if opturno == "a":
                turno = "M"
            elif opturno == "b":
                turno = "V"
            archivo =open("Alumnos.txt" , "r")
            lineas = archivo.readlines()
            archivo.close()
            for linea in lineas:
                linea = linea.strip()
                partes = linea.split(" ")
                if partes[4] == turno:
                    print(partes)
        elif op == 5:
            print("1.Aprobados")
            print("2.Reprobados")
            opcal = int(input("Elija una opcion: "))
            if opcal == 1:
                archivo =open("Alumnos.txt" , "r")
                lineas = archivo.readlines()
                archivo.close()
                for linea in lineas:
                    linea = linea.strip()
                    partes = linea.split(" ")
                    if int(partes[5]) >= 6: 
                        print(partes)
            elif opcal == 2:
                archivo =open("Alumnos.txt" , "r")
                lineas = archivo.readlines()
                archivo.close()
                for linea in lineas:
                    linea = linea.strip()
                    partes = linea.split(" ")
                    if int(partes[5]) < 6: 
                        print(partes)
    elif opcion == 3:
        nombre = input("Ingrese el nuevo nombre:")
        edad = input("Edad: ")
        grado = input ("Grado:")
        grupo = input("Grupo: ")
        turno = input("Turno: ")
        calificacion = input("Calificacion: ")
        archivo  = open("Alumnos.txt" ,"a")
        archivo.write(f"\n{nombre} {edad} {grupo} {turno} {calificacion}")
        archivo.close()
        archivo =open("Alumnos.txt" , "r")
        lineas = archivo.readlines()
        archivo.close()
        for linea in lineas:
            linea = linea.strip()
            partes = linea.split(" ")
            print(partes)
    elif opcion == 4:
        encontrado = False
        archivo = open("Alumnos.txt" , "r")
        datos = [linea.strip().split() for linea in archivo]
        alumno = input("¿Que alumno desea modificar?")
        for fila in datos:
            if fila[0] == alumno :
                encontrado = True
                print("1.Nombre")
                print("2.Edad")
                print("3.Grado")
                print("4.Grupo")
                print("5.Calificacion")
                print("6.Finalizar")
                op = int(input("¿Que desea modificar?"))
                if op == 1: 
                    nuevonombre = input("Ingrese el nuevo nombre: ")
                    fila[0] = nuevonombre
                    archivo = open("Alumnos.txt" , "w")
                    for fila in datos:
                        archivo.write(" ".join(fila) + "\n")
                elif op == 2:
                    nuevaedad = input("Ingrese la nueva edad: ")
                    fila[1] = nuevaedad
                    archivo = open("Alumnos.txt" , "w")
                    for fila in datos:
                        archivo.write(" ".join(fila) + "\n")
                elif op == 3:
                    nuevogrado = input("Ingrese el nuevo grado: ")
                    fila[2] = nuevogrado
                    archivo = open("Alumnos.txt" , "w")
                    for fila in datos:
                        archivo.write(" ".join(fila) + "\n")
                elif op == 4:
                    nuevogrupo = input("Ingrese el nuevo grupo: ")
                    fila[3] = nuevogrupo 
                    archivo = open("Alumnos.txt" , "w")
                    for fila in datos:
                        archivo.write(" ".join(fila) + "\n")
                elif op == 5:
                    nuevoturno = input("Ingrese el nuevo turno: ")
                    fila[4] = nuevoturno
                    archivo = open("Alumnos.txt" , "w")
                    for fila in datos:
                        archivo.write(" ".join(fila) + "\n")
                elif op == 6:
                    nuevacalificacion = input = ("Ingrese la nueva calificacion: ")
                    fila[5] = nuevacalificacion
                    archivo = open("Alumnos.txt" , "w")
                    for fila in datos:
                        archivo.write(" ".join(fila) + "\n")
    elif opcion == 5:
        encontrado = False
        nelim = input("Ingrese el nombre del alumno que desea eliminar: ")
        archivo =open("Alumnos.txt" , "r")
        datos = [linea.strip().split() for linea in archivo]
        #print(datos)
        archivo.close()
        for linea in datos:
            #print(linea[0], nelim)
            if linea[0].strip().lower() == nelim.strip().lower():
                datos.remove(linea)
                encontrado = True
        if encontrado:
            archivo = open("Alumnos.txt" , "w")
            for fila in datos:
                archivo.write(" ".join(fila) + "\n")
            archivo.close()
            print("Eliminado con exito")
        else:
            print("No se encontro el alumno")   
    elif opcion == 6:
        archivo =open("Alumnos.txt" , "r")
        datos = [linea.strip().split() for linea in archivo]
        archivo.close()
        print("1.Completa")
        print("2.Por grado")
        print("3.Por grupo")
        print("4.Por turno")
        print("5.Aprobados o reprobados")
        opimprimir = int(input("ELija una opcion"))
        if opimprimir == 1:
            for lista in datos:
                print(lista)
        elif opimprimir == 2:
            gradoimpr = input("Ingrese el grado que desea buscar: ")
            archivo = open("Alumnos.txt", "w") 
            for lista in datos:
                if lista[2] == gradoimpr:
                    archivo.write(f"{lista}\n")
                    print(lista)
            archivo.close()
        elif opimprimir == 3:
            gradoimpr = input("Ingrese el grupo que desea buscar: ")
            archivo = open("Alumnos.txt", "w") 
            for lista in datos:
                if lista[3] == gradoimpr.upper():
                    archivo.write(f"{lista}\n")
                    print(lista)
            archivo.close()
        elif opimprimir == 4:
            gradoimpr = input("Ingrese el turno que desea buscar: ")
            print("M = matutino\nV = vespertino")
            archivo = open("Alumnos.txt", "w") 
            for lista in datos:
                if lista[4] == gradoimpr.upper():
                    archivo.write(f"{lista}\n")
                    print(lista)
            archivo.close()
        elif opimprimir == 5:
            print("1.Aprobados")
            print("2.Rerpobados")
            opcali = int(input("Elige una opcion:"))
            if opcali == 1:
                archivo = open("Alumnos.txt", "w") 
                for lista in datos:
                    if lista[5] >= 6:
                        archivo.write(f"{lista}\n")
                        print(lista)
                archivo.close()
            elif opcali == 2:
                archivo = open("Alumnos.txt", "w") 
                for lista in datos:
                    if lista[5] < 6:
                        archivo.write(f"{lista}\n")
                        print(lista)
                archivo.close()
            else:
                print("Opcion no valida")