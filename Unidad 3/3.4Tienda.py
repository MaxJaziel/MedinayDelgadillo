opusuario = 0
primermenu = 0
carrito = []
opcliente = 0
#medina morelos
while primermenu != 3:
    print("¿Qué eres?")
    primermenu = int(input("1. Cliente\n2. Vendedor\n3. Salir\n"))
    if primermenu == 1:
        opcliente = 0
        while opcliente != 5:
            print("\n1. Agregar producto al carrito")
            print("2. Eliminar producto del carrito")
            print("3. Mostrar total del carrito")
            print("4. Pagar")
            print("5. Salir usuario\n")
            opcliente = int(input("Elija una opción: "))
            if opcliente == 1:
                archivo = open("Unidad 3/Productos.txt", "r")
                datos = [linea.strip().split() for linea in archivo]
                archivo.close()
                finalizar = False
                while not finalizar:
                    for linea in datos:
                        print(linea)
                    carritoagg = input("Nombre del producto a agregar: ")
                    encontrado = False
                    for linea in datos:
                        if linea[1] == carritoagg:
                            encontrado = True
                            while encontrado == True :
                                cantidad = int(input("¿Cuántos?: "))
                                if cantidad >= int(linea[2]):
                                    print("Ingrese una cantidad valida")
                                    encontrado = False
                                precio = int(linea[3])
                                productoagg = [linea[1], precio, cantidad, cantidad * precio]
                                carrito.append(productoagg)
                                encontrado = False
                    print("1. Agregar otro producto")
                    print("2. Finalizar")
                    if int(input(" ")) == 2:
                        finalizar = True
                print("\nCarrito actual:")
                for p in carrito:
                    print(p)
            elif opcliente == 2:
                carritodel = input("Nombre del producto a eliminar: ")
                for prod in carrito:
                    if prod[0] == carritodel:
                        cantidaddel = int(input("¿Cuántos deseas eliminar?: "))
                        prod[2] -= cantidaddel
                        if prod[2] <= 0:
                            carrito.remove(prod)
                        print(carrito)
            elif opcliente == 3:
                total = 0
                for producto in carrito:
                    print(producto)
                    total += producto[3]
                print("Total: ", total)
            elif opcliente == 4:
                total = 0
                for producto in carrito:
                    print(producto)
                    total += producto[3]
                print(f"El total a pagar es: {total}")
                cambio = int(input("¿Con cuánto paga?: "))
                if cambio < total:
                    cambiovalido = False
                    print("Da una cantidad valida")
                elif cambio > total:
                    print("Su cambio es: ", cambio - total)
    elif primermenu == 2:
        opusuario = 0
        while opusuario != 6:
            print("\n1. Importar archivo")
            print("2. Mostrar inventario")
            print("3. Agregar/modificar producto")
            print("4. Eliminar producto")
            print("5. Guardar archivo")
            print("6. Salir de usuario")
            opusuario = int(input("\n"))
            if opusuario == 1:
                print("1. Sustituir parametros actuales")
                print("2. Agregar existencias")
                op_imp = int(input("Elija una opción: "))
                with open("Unidad 3/Productos.txt", "r") as archivo:
                    datos = [linea.strip().split() for linea in archivo]
                if op_imp == 1:
                    for item in carrito:
                        for prod in datos:
                            if prod[1] == item[0]:
                                prod[2] = str(int(prod[2]) - item[2])
                    print("Existencias descontadas")
                elif op_imp == 2:
                    nombre = input("Nombre del producto: ")
                    cantidad = int(input("¿Cuántas existencias agregarás?: "))
                    for prod in datos:
                        if prod[1] == nombre:
                            prod[2] = str(int(prod[2]) + cantidad)
                            print("Existencias agregadas")
                with open("Unidad 3/Productos.txt", "w") as archivo:
                    for linea in datos:
                        archivo.write(" ".join(linea) + "\n")
                print("Inventario actualizado")
            elif opusuario == 2:
                print("\n1. Todos")
                print("2. Por nombre")
                print("3. Por ID")
                op_impr = int(input("Elija opción: "))
                archivo = open("Unidad 3/Productos.txt", "r")
                lineas = archivo.readlines()
                archivo.close()
                if op_impr == 1:
                    for linea in lineas:
                        print(linea.strip().split())
                elif op_impr == 2:
                    nombre = input("Nombre: ")
                    for linea in lineas:
                        partes = linea.strip().split()
                        if partes[1] == nombre:
                            print(linea)
                elif op_impr == 3:
                    id = input("ID: ")
                    for linea in lineas:
                        partes = linea.strip().split()
                        if partes[0] == id:
                            print(linea)
            elif opusuario == 3:
                print("1. Agregar producto")
                print("2. Modificar producto")
                op = int(input("Elija opción: "))
                if op == 1:
                    nombre = input("Nombre: ")
                    existencias = input("Existencias: ")
                    precio = input("Precio: ")
                    archivo = open("Unidad 3/Productos.txt", "r")
                    lineas = archivo.readlines()
                    archivo.close()
                    ultimo_id = int(lineas[-1].split()[0])
                    nuevo_id = ultimo_id + 1
                    with open("Productos.txt", "a") as archivo:
                        archivo.write(f"{nuevo_id} {nombre} {existencias} {precio}\n")
                    print("Agregado")
                elif op == 2:
                    nombremod = input("Nombre del producto: ")
                    with open("Productos.txt", "r") as archivo:
                        datos = [linea.strip().split() for linea in archivo]
                    for linea in datos:
                        if linea[1] == nombremod:
                            opmod = 0
                            while opmod != 4:
                                print("1.Nombre\n2.Existencias\n3.Precio\n4.Finalizar")
                                opmod = int(input("Opción: "))
                                if opmod == 1:
                                    linea[1] = input("Nuevo nombre: ")
                                elif opmod == 2:
                                    linea[2] = input("Nueva existencia: ")
                                elif opmod == 3:
                                    linea[3] = input("Nuevo precio: ")
                    with open("Productos.txt","w") as archivo:
                        for linea in datos:
                            archivo.write(" ".join(linea)+"\n")
                    print("Modificado")
            elif opusuario == 4:
                print("1.Eliminar por ID")
                print("2.Eliminar por nombre")
                opeliminar = int(input("Elija opción: "))
                archivo = open("unidad 3/Productos.txt", "r")
                datos = [linea.strip().split() for linea in archivo]
                archivo.close()
                if opeliminar == 1:
                    iddel = input("ID: ")
                    datos = [l for l in datos if l[0] != iddel]
                elif opeliminar == 2:
                    nombredel = input("Nombre: ")
                    datos = [l for l in datos if l[1] != nombredel]
                print("Eliminado")
            elif opusuario == 5:
                with open("Unidad 3/Productos.txt", "w") as archivo:
                    for linea in datos:
                        archivo.write(" ".join(linea) + "\n")
                print("Guardado")