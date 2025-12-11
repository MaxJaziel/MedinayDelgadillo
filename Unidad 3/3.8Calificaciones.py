def leer_archivo():
    with open("Unidad 3/Alumnos.txt" ,"r")as archivo :
        datos = [linea.strip().split() for linea in archivo]
        for o in datos:
            print(o)

def mostrar():
    op = 0
    while op != 7:
        print("1.Completa")
        print("2.Por grado")
        print("3.Por grupo")
        print("4.Por turno")
        print("5.Aprobados o reprobados")
        op = int(input("ELija una opcion: "))
        if op == 1:
            with open("Alumnos.txt" , "r") as archivo:
                datos = [linea.strip().split()for linea in archivo]
                print(datos)
        elif op == 2:
            grado = input("¿Que grado desea mostrar?: ")
            with open("Alumnos.txt" , "r") as archivo:
                datos = [linea.strip().split()for linea in archivo]
                for o in datos:
                    if o[2] == grado:
                        print(o)
        elif op == 3:
            grupo = input("¿Que grupo desea mostrar?: ")
            with open("Alumnos.txt" , "r") as archivo:
                datos = [linea.strip().split()for linea in archivo]
                for o in datos:
                    if o[3] == grupo:
                        print(o)
        elif op == 4:
            print("a)Matutino")
            print("b)Vespertino")
            opturno = input("¿Que turno desea mostrar?")
            if opturno == "a":
                turno = "M"
            elif opturno == "b":
                turno = "V"         
            with open("Alumnos.txt" , "r") as archivo:
                datos = [linea.strip().split()for linea in archivo]
                for o in datos:
                    if o[4] == grupo:
                        print(o)
        elif op == 5:
            print("1.Aprobados")
            print("2.Reprobados")
            opcal = int(input("Elija una opcion: "))
            if opcal == 1:
                with open("Alumnos.txt" , "r") as archivo:
                    datos = [linea.strip().split()for linea in archivo]
                    for o in datos:
                        if int(o[5]) >= 6:
                            print(o)
            if opcal == 1:
                with open("Alumnos.txt" , "r") as archivo:
                    datos = [linea.strip().split()for linea in archivo]
                    for o in datos:
                        if int(o[5]) < 6:
                            print(o)
def agregar_alumno():

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
        leer_archivo()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        agregar_alumno()
    elif opcion == 4: