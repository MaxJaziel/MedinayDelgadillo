#Lista 
alumnos =["Ana","Luis","Maria","Pedro","Lucia"]
#Tupla
materias = ("Matematicas","Historia","Ciencias")
#Diccionario
promedios = {"Ana": 85 ,"Luis": 90,"Maria":78 ,"Pedro": 92,"Lucia": 88}
#Conjunto
aprobados = set()
#Alumnos y calificaciones
for nombre in alumnos:
    promedio = promedios[nombre]
    print(f"{nombre}:{promedio}")
    if promedio > 70:
        aprobados.add(nombre)
print("Alumnos:", alumnos)
print("Materias(tupla):",materias)
print("Aprobados(set):",aprobados)
print("Diccionario de promedios:",promedios)
promedio_general=sum(promedios.values())/len(promedios)
print("\nPromedio general del grupo:",round(promedio_general,2))