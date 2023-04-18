# bandera o flag

esMayorDeEdad = False

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    esMayorDeEdad = True

if esMayorDeEdad:
    print("Puede entrar a ver la película")
else:
    print("No puede entrar al cine")