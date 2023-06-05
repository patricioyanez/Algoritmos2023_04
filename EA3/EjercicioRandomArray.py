#Ejercicios:

# 1.1 Crear un arreglo unidimensional de tamaño 10, 
# con valores aleatorios de números enteros del 0 al 100, 
# para ello deberá investigar la función que 
# permita crear números aleatorios.
# 
# 1.2. Crear una copia del arreglo y muestre:
# Elemento mayor
# Elemento menor
# Suma de los elementos
# Promedio de los elementos
# Mostrar todos los elementos

# pip list 
# para instalar, ejecutar:
# pip install numpy

import numpy as np 
numero = np.random.randint(100)

print(numero)

arreglo = np.random.randint(100, size=(10))
print(arreglo)

arreglo2 = arreglo.copy()
print("Mayor:", arreglo2.max())
print("Minimo:", arreglo2.min())
print("Suma:", arreglo2.sum())
print("Suma:", arreglo2.mean())

# recorro y muestro el valor de cada item
for valor in arreglo2:
    print("Valor:", valor)

