# instalar libreria: pip install numpy

import numpy as np

arreglo = np.array([1,5,7,3,6,10,55,45,11,77])
print(arreglo)

print("Cantidad de dimensiones: ", arreglo.ndim)
print("Cantidad de elementos  : ", len(arreglo))
print("Valor del indice 2     : ", arreglo[2])
print("Cortar una porción     : ", arreglo[2:7])
print("Cortar una porción     : ", arreglo[2:7:2])
print("Último valor           : ", arreglo[-1])
print("AntePenÚltimo valor    : ", arreglo[-3])


# crear arreglo de forma rapida
arreglo1 = np.arange(10,100)
print(arreglo1)

arreglo2 = [i for i in range(10)]
print(arreglo2)


# recorrer un arreglo
for i in range(len(arreglo1)): # 0 .. 9
    print(arreglo1[i])


# operaciones con arreglo
arr1 = np.array([ 1, 12, 30, 14,150])
arr2 = np.array([10, 12,  3, 14, 50])

resultado = arr1 + arr2
print(resultado)
resultado = arr1 - arr2
print(resultado)
resultado = arr1 * arr2
print(resultado)
resultado = arr1 / arr2
print(resultado)