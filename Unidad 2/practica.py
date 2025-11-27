opcion = 0
jugadores ={
    "max":{"goles_anotados":2,"partidos_jugados": 4,"posicion":"delantero"},
    "moctezuma":{"goles_anotados": 4,"partidos_jugados": 6,"posicion":"portero"},
    "areli":{"goles_anotados": 6,"partidos_jugados": 2,"posicion":"defensa"}
}
while opcion != 7:
    print("1.Registrar jugadores \n2.Mostrar 1ista completa del equipo")
    print("3.Mostrar los jugadores que tienen promedio de un gol o mas por partido")
    print("4.Mostrar el jugador con mas goles y el que tenga menos")
    print("5.Preguntar una posicion y decir cuantos jugadores juegan ahi")
    print("6.Editar jugador")
    print("7.Salir del programa\n")
    opcion = int(input("Elige una opcion:\n"))
    if opcion == 1:
        jugador_agg = input("Ingrese el nombre del nuevo jugador")
        if jugador_agg in jugadores:
            print("Ese jugador ya existe")
        else:
            golesa_agg = int(input("Ingresa los goles anotados: "))
            partidos_agg = int(input("Ingresa los partidos jugados: "))
            posicion_agg = input("Ingresa la posicion que juega: ")
            jugadores[jugador_agg] = {"goles_anotados" : golesa_agg, "partidos_jugados" : partidos_agg,"posicion": posicion_agg}
            print(jugadores)
    elif opcion == 2:
        print(f"{jugadores}\n")
    elif opcion == 3:
        for jugador in jugadores:
            golesa = jugadores[jugador]["goles_anotados"]
            partidosj = jugadores[jugador]["partidos_jugados"]
            if partidosj > 0:
                promedio = golesa / partidosj
                if promedio >= 1:
                    print(f"\n{jugador} , Promedio : {promedio}\n")
    elif opcion == 4:
        maximo= -1
        minimo= 99
        jugadormax= ""
        jugadormin=""
        
        for jugador in jugadores:
            golesa = jugadores[jugador]["goles_anotados"]
            if golesa > maximo:
                maximo = golesa
                jugadormax = jugador
            if golesa < minimo:
                minimo = golesa
                jugadormin = jugador
        print(f"\nMaximo goleador: {jugadormax}, Goles anotados: {maximo}")
        print(f"Minimo goleador: {jugadormin}, Goles anotados: {minimo}\n")
    elif opcion == 5:
        print("\nPosiciones:")
        print("-delantero")
        print("-defensa")
        print("-medio")
        print("-portero")
        posicionbusc = input("¿Que posicion desea buscar?:")
        posiciones= 0
        for jugador in jugadores:
            if jugadores[jugador]["posicion"] == posicionbusc:
                posiciones += 1
        print(f"En total juegan {posiciones} en esa posicion\n")
    elif opcion == 6:
        print(jugadores)
        jugadoredit = input("¿Que jugador desea editar?:")
        if jugadoredit in jugadores:
            print("1. Editar goles anotados")
            print("2. Editar partidos jugados")
            print("3. Editar posición")
            opcion_edit = int(input("Elige una opción: \n"))
            if opcion_edit == 1:
                jugadores[jugadoredit]["goles_anotados"] = int(input("Nuevos goles anotados: "))
                print("se registraron los nuevos goles anotados\n")
            elif opcion_edit == 2:
                jugadores[jugadoredit]["partidos_jugados"] = int(input("Nuevos partidos jugados: "))
                print("se registraron los nuevos partidos anotados\n")
            elif opcion_edit == 3:
                jugadores[jugadoredit]["posicion"] = input("Nueva posición: ")
                print("se ha registrado la nueva posicion\n")
            else:
                print("Opción no válida")
        else:
            print("Ese jugador no existe")
    elif opcion == 7:
        print("Has salido del programa")
    else:
        print("Opción no válida")