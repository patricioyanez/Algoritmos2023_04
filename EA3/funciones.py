#FUNCIONES

# definir una función
def saludo():
    # codigos de la funcion
    print("Hola Mundo de las funciones")


#llamar función declarada
saludo()

# 2.- función con opcion de retorno
def sumar():
    numero1 = 10
    numero2 = 20
    return numero1 + numero2


total = sumar()
print("El total es:",total)


# 3.- funcion con parametros y retorno
def restar(numero1, numero2):
    return numero1 - numero2

# llamar función
total = restar(10,7)
print("El total es:",total)

#4.- función sin retorno
def restar2(numero1, numero2):
    print("\nTotal:", numero1 - numero2)

restar2(50,10)