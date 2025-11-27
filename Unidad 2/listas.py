nums= [5, 2, 9, 2, 7]
print("Lista: ", nums)

print("Primer valor: " ,nums[0])
print("Ultimo valor: " ,nums[-1])
print("Valores de la posición:[1-4]: " ,nums[1:4])
print("Indice de 9: " ,nums.index(9))
print("Contador de 2: " ,nums.count(2))

nums.append(10)
print("Lista: ",nums)
a= nums.pop()
b=nums.pop(0)
print ("a: ",a)
print ("b: ",b)
print("Lista despues de pops: ", nums)

nums.sort()
print("Lista ordenada: ", nums)
nums.sort(reverse= True)
print("Ordenamiento descendente: ", nums)
nums.reverse()
print("Invertir lista: ",nums)

copia=nums.copy()
nums.clear()
print("Copia: ", copia)
print("Lista despues de clear: ", nums)

print("Longitud copia: ", len(copia))
print("Está el 99 en la lista?: ", 99 in copia)
print("Concatenación: ", copia + [1,2,3])
print("Repetir: ", [1,2,3]*3)