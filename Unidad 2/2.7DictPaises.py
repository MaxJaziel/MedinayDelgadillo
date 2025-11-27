
#pais_enc=0
pais_buscado=0
se_encontro = False
paises = {
    "mexico" : {"capital" : "cdmx","poblacion": 1260000},
    "eua" : {"capital": "washington dc","poblacion" : 702250},
    "argentina" : {"capital" : "buenos aires","poblacion" : 3121707 },
    "peru" : {"capital" : "lima", "poblacion" : 10400000},
    "francia" : {"capital" : "paris", "poblacion" : 2048472 }
}
salida = 1
while salida !=6:
    print("\n1.Mostrar todos los paises")
    print("2.Buscar pais")
    print("3.Agregar nuevo pais")
    print("4.Modificar informacion")
    print("5.Eliminar pais")
    print("6.Salida")
    salida = int(input("Seleccione una opcion:"))
    if salida == 1:
        print(paises)
    elif salida == 2:
        pais_buscado =input("¿Que pais desea buscar?\n")
        for pais in paises:
            if pais == pais_buscado:
                print(f"{pais} : {paises[pais]}")    
                se_encontro= True
        if se_encontro == False:
                print("No se encontro el pais")
    elif salida == 3:
        pais_agg = input("¿Que pais deseas agregar?")
        if pais_agg in paises:
            print("Ese pais ya existe")
        capital_agg =input("¿Cual es la capital del pais?")
        poblacion_agg = input("¿Cual es su poblacion?")
        paises[pais_agg] ={"capital" : capital_agg ,"poblacion" : poblacion_agg}
        print(paises)
        print("Pais agregado exitosamente")
    elif salida == 4:
        pais_mod = input("Que pais desea modificar: ")
        for pais in paises:
            pais = pais_mod
        print("1.capital")
        print("2.poblacion")
        opcion_mod = int(input("¿Que desea modificar?"))
        if opcion_mod == 1:
            capital_mod = input("Ingrese la capital nueva: ")
            paises[pais]["capital"] = capital_mod
            print(pais,paises[pais])
            print("modificado con exito")
        elif opcion_mod == 2:
            poblacion_mod = input("Ingrese la poblacion: ")
            paises[pais]["poblacion"] = poblacion_mod
            print(pais,paises[pais])
            print("modificado con exito")
    elif salida ==5:
        pais_eliminar = input("¿Que pais desea eliminar?")
        if pais_eliminar in paises:
            paises.pop(pais_eliminar)
            print("Pais eliminado correctamente")
        else:
            print("Ese pais no se encuentra en la lista")
        print(paises)
    elif salida == 6:
        print("Programa finalizado")
        