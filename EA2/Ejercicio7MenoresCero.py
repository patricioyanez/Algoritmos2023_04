print("Contar números menores a cero")
n1 = int(input("ingrese 1er número:"))
n2 = int(input("ingrese 2do número:"))
n3 = int(input("ingrese 3er número:"))
contador = 0
if n1 < 0:
    contador+=1
if n2 < 0:
    contador+=1
if n3 < 0:
    contador+=1

print("El total de números negativos son:", contador)