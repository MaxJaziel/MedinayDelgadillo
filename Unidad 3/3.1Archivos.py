#Crear un archivo nuevo y escribir texto
archivo = open("demo.txt", "w") #write
archivo.write("Primera linea de texto\n")
archivo.write("Segunda linea de texto\n")
archivo.write("Tercera linea de texto\n")
archivo.close()
print("El archivo 'demo.txt' creado con 3 lineas")

#Ingresar mas contenido con append
archivo = open("demo.txt", "a")
archivo.write("Cuarta linea agregada con modo append\n")
archivo.write("Quinta linea agregada con modo append\n")
archivo.close()
print("Se agregaron 3 lineas nuevas al final del archivo")

#leer todo el contenido con read 
archivo = open("demo.txt" , "r")
contenido = archivo.read()
archivo.close()
print("contenido completo del archivo:")
print(contenido)
print(" ")

#leer linea por linea con readline 
archivo = open ("demo.txt", "r")
linea1 = archivo.readline()
linea2 = archivo.readline()
archivo.close()
print("Primera linea :",linea1)
print("Segunda linea : " , linea2)

#Leer todas las lineas con readlines()
archivo = open("demo.txt", "r")
lineas = archivo.readlines()
archivo.close()
print("Lista de lineas (incluye saltos de linea '\\n'):")
print(lineas)

#Leer el archivo con un ciclo for 
archivo = open("demo.txt", "r")
for linea in archivo:
    print(linea.strip())
archivo.close()

#Sobreesrcibir el archivo con nuevo contenido 
archivo = open("demo.txt", "w")
archivo.write("Nuevo contenido\n")
archivo.write("EL archivo fue sobreescrito por completo\n")
archivo.write ("Ya no existen las lineas anteriores \n")
archivo.close()
print("El archivo fue sobreescrito")