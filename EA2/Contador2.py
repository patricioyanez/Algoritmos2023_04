print("***  Contador de número pares  ***")
contador = 0

numero = int(input("Ingrese 1er número: "))
if numero % 2 == 0:
    contador = contador + 1
    
numero = int(input("Ingrese 2do número: "))
if numero % 2 == 0:
    contador += 1 # otra forma de aumentar en 1 el valor de contador

numero = int(input("Ingrese 3er número: "))
if numero % 2 == 0:
    contador = contador + 1

print("La cantidad de número pares son: ", contador)