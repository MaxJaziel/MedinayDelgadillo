estudiantes = {}
calmayor = 0
calificaciones = 0
for i in range(1,6):
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad :"))
    cal = int(input("Ingresa la calificacion final (1-100): "))
    estudiantes = {"nombre" : nombre ,"edad" : edad,"calificacion" : cal}
    calificaciones = calificaciones + cal
    if cal >= 80:
        print(estudiantes["nombre"])
    promedio = calificaciones / 5
    for e in estudiantes:
        cal = estudiantes["calificacion"]
        if cal > calmayor:
            calmayor = cal
print(estudiantes)
print("El promedio es:" , promedio)
print("La calificacion myaor es :" ,calmayor)