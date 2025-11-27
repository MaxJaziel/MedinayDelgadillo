promedio = 0
reprobados = 0
aprobados = 0
maxima = 0
minima = 100 
alumnos = int(input("¿Cual es el numero de alumnos?"))
for i in range (1, alumnos+1):
    cal = int(input (f"ingrese la calificacion del alumno {i}:"))
    if cal > maxima:
        maxima = cal
    if cal < minima:
        minima = cal 
    if cal <= 60 :
        reprobados += 1
    elif cal > 60:
        aprobados += 1 
    promedio = promedio + cal 
    
promediof = promedio / alumnos   
print("Elige una opcion:")
print("1.Mostrar promedio ,maximo y minimo")
print("2.Mostrar conteo de aprobados y reprobados,porcentaje de ambos")
print("3.Clasificar el promedio")
opcion = int(input(""))
match opcion:
    case 1: 
        print(f"El promedio es {promediof} \nLa calificacion maxima es {maxima} y la minima es {minima}")
    case 2:
        print(f"Aprobados:{aprobados}\nReprobados: {reprobados}")
        porcentajea = aprobados * 100 / alumnos 
        porcentajer = reprobados * 100 / alumnos 
        print(f"Porcentaje total: \n Aprobados {porcentajea}% \n Reprobados: {porcentajer}% ")
    case 3:
        print(f"Promedio:{promediof}")
        if promediof >=  90:
            print("Excelente")
        elif promediof >= 60:
            print("Aprobado!")
        elif promediof <60:
            print("Reprobado")