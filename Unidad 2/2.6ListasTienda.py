productos = ["Leche","Huevos","Arroz","Platanos","Galletas","PanIntegral","CocaCola","Dulces","Agua","Tostadas"]
precios = [20,56,12,10,22,30,23,2,15,25]
salida = 1
compra = 1
preciofinal =0
r_precios =[]
r_productos = []
r_cantidad = []
i = 0
print("1.Leche\n2.Huevos\n3.Arroz\n4.Platanos\n5.Galletas\n6.PanIntegral\n7.CocaCola\n8.Dulces\n9.Agua\n10.Tostadas")
while salida !=2:
    while compra != 2:
        compra= int(input("¿Que producto desea comprar?"))
        sel_precio = precios[compra-1]
        sel_precio2 = precios[compra-1]
        r_precios.append(sel_precio)
        sel_productos = productos[compra-1]
        r_productos.append(sel_productos)
        cantidad = int(input("¿Cuantos?"))
        r_cantidad.append(cantidad)
        precionofinal = sel_precio * cantidad
        preciofinal += precionofinal
        print("¿Algun otro producto?\n1.si\n2.No")
        compra = int(input())
    salida=2
print("Producto mas caro:",max(r_precios))
print("Producto mad barato:",min(r_precios))
print("\nRecibo")
print("Producto Precio Cantidad")
for i in range (len(r_productos)):
    print(f"{r_productos[i]}      {r_precios[i]}      {r_cantidad[i]} ")
print("Total:",preciofinal)
