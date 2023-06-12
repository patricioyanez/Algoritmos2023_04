import numpy as np
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Valor F1 C1:", matriz[1,1] )
print("Valor F2 C0:", matriz[2,0] )

# recorrer la matriz
for fila in range(3):
    for columna in range(3):
        print("valor:", matriz[fila,columna])

print(matriz)

print("Coordenada y su valor")
for fila in range(3):
    for columna in range(3):
        print("Fila: ", fila, "Columna: ", columna, "Valor: ", matriz[fila,columna])


# métodos utiles
matriz1 = np.zeros((4,3))
print(matriz1)
matriz1 = np.ones((4,4))
print(matriz1)
matriz1 = np.diag([2,4,6,7])
print(matriz1)

print("Suma de valores:", matriz.sum())
print("cant. elemento  matriz:", matriz.size)
print("tamaño  matriz:", matriz.shape)


matriz1 = np.diag(["","","","",""])
print(matriz1)