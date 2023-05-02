# Ingrese por teclado 10 letras, 
# indique cuantas de ellas son vocales y 
# cuántas son consonantes.

rango = range(10)
vocales = 0
consonantes= 0
for x in rango:
    letra = input("Ingrese una letra:")

    #if letra == "a" or letra == "e"....

    if letra.lower() in ("a", "e", "i", "o", "u"): ## upper() mayuscula
        vocales +=1
    else:
        consonantes += 1

# resultados
print("Vocales      : ", vocales)
print("Consonantes  : ", consonantes) 