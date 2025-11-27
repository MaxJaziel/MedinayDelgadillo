jugadores = { 
    "max" : {"goles_anotados" : 2 , "partidos_jugados" : 4 , "posicion" : "delantero"},
    "emiliano" : {"goles_anotados" : 4, "partidos_jugados" : 6, "posicion" : "portero"},
    "arely" : {" goles_anotados" : 6, "partidos_jugados" : 2, "posicion" : "defensa"}
}
print("1.Registrar jugadores\n2.Mostrar lista completa del equipo")
print("3.Mostrar los jugadores que tienen promedio de un gol o mas por partido")
print("4.Mostrar el jugador con mas goles y el que tenga menos")
print("5.Preguntar una posicion y decir cuantos jugadores juegan ahi")
print("6.Editar jugador")
print("7.Salir del programa")

opcion = int(input("Elige una opcion: "))
if opcion == 1:
    jugador_agg = input("Ingresa el nombre del nuevo jugador")
    if jugador_agg in jugadores:
        print("Ese jugador ya esta registrado: ")
    golesa_agg = input("Ingresa los goles anotados: ")
    partidosa_agg = input("Ingresa los partidos jugados:")
    posicion_agg = input("En que posicion juega:")
    jugadores[jugador_agg] = {"goles_anotados" : golesa_agg , "partidos_jugados" : partidosa_agg, "posicion" : posicion_agg }
    print(jugadores[jugador_agg])
    print("Agregado con exito")
elif opcion == 2:
    print(jugadores)
elif opcion == 3:
    for jugador in jugadores:
        promedio = int(jugadores[jugador]["goles_anotados"]) / int(jugadores[jugador]["partidos_jugados"])
        if promedio > 1:
            print(f"{jugador} {jugadores[jugador]}")