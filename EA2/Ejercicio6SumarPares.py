# sumar pares mayores a cero
print("Suma de números mayores a cero y pares")
n1 = int(input("ingrese 1er número:"))
n2 = int(input("ingrese 2do número:"))
n3 = int(input("ingrese 3er número:"))
contador = 0
suma = 0

if n1 > 0 and n1 % 2 == 0:
    suma += n1 # suma = suma + n1
else:
    contador+=1
if n2 > 0 and n2 % 2 == 0:
    suma += n2 
else:
    contador+=1
if n3 > 0 and n3 % 2 == 0:
    suma += n3 
else:
    contador+=1

print("El total de la suma es:", suma)
print("Cantidad de números impares y cero: ", contador)