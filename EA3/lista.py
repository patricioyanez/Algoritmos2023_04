# listas

lista = [100, "a", True, 2.5]

print(lista)

print("Valor del indice 1:", lista[1])
print("Valor del indice 3:", lista[3])
#indice   0   1  2  3
lista2 = [10,20,30,40]
#indece   -4 -3 -2 -1 
print("El valor del indice 1:", lista2[1])
print("La cantidad de elementos son:", len(lista2))
print("El valor del indice -1:", lista2[-1]) # es el último elemento
print("El valor del indice -2:", lista2[-2]) # es el último elemento
print(lista2)
lista2.append(1000)
print(lista2)

print("La cantidad de elementos son:", len(lista2))

# pip install numpy
# black box
lista2.reverse() # invierte los valores de un arreglo
print(lista2)


# agregar elemento en indice diferente

lista2.insert(3, 5000)
print(lista2)

lista3 = ["a", "b"]
# une 2 listas en una sola
lista2.extend(lista3)
print(lista2)
print(lista3)