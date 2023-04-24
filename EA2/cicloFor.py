### ciclo for

rango = range(5) # 0,1,2,3,4
for numero in rango:
    print(numero)

print("\n ======== cambio de inicio del rango")
rango = range(1,6)
for numero in rango:
    print(numero)

print("\n ======== cambio de aumento del rango")
rango = range(1,10, 2)
for numero in rango:
    print(numero)
print("\n ======== Números pares")
contador = 0
rango = range(2,11, 2)
for numero in rango:
    print(numero)
    contador += 1
print("iteró ", contador, " veces")

print("\n ======== Extracción de caracteres a un texto")
contador = 0
nombre = "Fernanda"
for letra in nombre:
    print("La letra es: ", letra)
    contador+=1
print("Cantidad de letras:",contador)