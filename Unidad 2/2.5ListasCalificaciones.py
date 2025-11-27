n = int(input("Cuantas calificaciones desea ingresar: "))
calificaciones = []
aprobados = []
reprobados = []
for i in range (1,n + 1):
    o = int(input("Ingrese la calificacion: "))
    calificaciones.append(o)
    if o >= 70 :
        aprobados.append(o)
    else :
        reprobados.append(o)
promedio = sum(calificaciones) / len(calificaciones)
print("\nCalificaciones :",calificaciones)
print("Promedio:" ,promedio)
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
calmax = max(calificaciones)
calmin = min(calificaciones)
print("Calificacion maxima:" ,calmax)
print("Calificacion minima:" ,calmin)
ordenado = sorted(calificaciones)
print("Calificaciones ordenadas:" ,ordenado)

