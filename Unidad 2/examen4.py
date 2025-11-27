productos = ["leche","pan","huevos" ,"queso","cereal","jugo","sopa"]
opcion = 0
while opcion != 5:
    print("1.Agregar producto")
    print("Eliminar un producto por nombre")
    print("3.Mostrar todos los productos")
    print("4.Buscar si un producto existe")
    print("5.Salir")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        prod = input("Ingresa el nuevo producto: ")
        productos.append(prod)
        print("Agregado con exito")
    elif opcion == 2:
        prodel = input("Ingresa el nombre del producto que deseas eliminar: ")
        for producto in productos:
            if producto == prodel:
                posicion = producto 
                productos.pop(1)
        print(productos)
    elif opcion == 3:
        print(productos)
    elif opcion == 4:
        prodbusc = input("Ingrese el producto que desea comprobar existencia")
        for producto in productos:
            if producto == prodbusc:
                print("Ese producto si existe")
