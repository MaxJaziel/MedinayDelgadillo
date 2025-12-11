
libros = [{"titulo": "La asistenta"   ,"autor" : "FreidaMcFadden"    ,"año" : 2000   ,"estatus" : "prestado"},
{"titulo" : "Grandeza", "autor" : "amlo" ,"año" : 2025 , "estatus": "disponible"},
{"titulo" : "La alegria" ,"autor" : "Benito Juarez" , "año" : 1999 , "estatus" : "presatado" },
{"titulo" : "Fuego" , "autor" : "Alejandro Rivera" , "año" : 1300 , "estatus" : "disponible" },
{"titulo" : "Perro " , "autor" : "Fernando Mtz." , "año" : 2026 , "estatus" : "prestado"},
{"titulo" : "El avance de la tecnologia ", "autor" : "Brandon Martinez" , "año" : 2025 , "estatus" : "prestado"},
{"titulo" : "La odisea" , "autor" : "Roberto Hernandez" , "año" : 2012, "estatus" : "disponible"},
{"titulo" : "Ecosistemas" , "autor" : "Brenda Venegas", "año" : 2018 , "estatus" : "prestado"}]
def registrar_libro():
    t = input("Ingresa el titulo del libro:")
    au = input("Ingresa el nombre del autor:")
    año = int(input("Ingresa el año publicacion :"))
    esta = input("Ingresa el estatus(disponible o prestado):")
    nuevolib = {"titulo" : t, "autor" : au , "año" : año ,"estatus" : esta} 
    libros.append(nuevolib)
    print("Libro agregado exitosamente")

def buscar_libro():
    librob = input("Ingresa el nombre del libro que quieres buscar: ")
    libroencontrado = False
    for libro in libros:
        if libro['titulo'] == librob:
            libroencontrado = True
            print(libro)
    if not libroencontrado:
        print("No se encontro\n")
opcion = 0
while opcion != 5:
    print("\n===Sistema de biblioteca====")
    print("1)Registrar libro")
    print("2)Mostar catalogo")
    print("3)Busca libro")
    print("4)Reportes a archivo")
    print("5)Salir")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        registrar_libro()
    elif opcion ==2:
        print(libros)
    elif opcion == 3:
        buscar_libro()
    elif opcion == 4:
        opr = 0
        while opr != 4:
            print("\n1)Guardar todos los libros")
            print("2)Guardar solo libros disponible")
            print("3)Guardar solo libros prestados")
            print("4)Regresar al menu principal")
            opr = int(input("Elige una opcion: "))
            if opr == 1:
                with open("Libros.txt" , "w") as archivo:
                    for libro in libros:
                        archivo.write(f"{libro}\n")
                print("Se guardo el archivo correctamente.")
            elif opr == 2:
                with open("Libros.txt" ,"w") as archivo:
                    for libro in libros:
                        if libro['estatus'] == "disponible":
                            archivo.write(f"{libro}\n")
                print("Se guardo el archivo correctamente.")
            elif opr == 3:
                with open("Libros.txt" ,"w") as archivo:
                    for libro in libros:
                        if libro['estatus'] == "prestado":
                            archivo.write(f"{libro}\n")
                print("Se guardo el archivo correctamente.")
            else:
                opr = 4