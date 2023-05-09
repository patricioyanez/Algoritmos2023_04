#I.- Caso: Máquina de Bebidas

# En su lugar de trabajo existe una máquina donde puede adquirir bebidas. Existen tres 
# opciones de bebida: Coca-Cola, Fanta y Sprite. El valor de cualquiera de ellas es: $400.
# Desarrolle un programa que permita vender una bebida y entregar vuelto si así se determina. 
# El programa debe solicitar por pantalla el tipo de bebida que va a comprar: 
# 1) Coca-Cola, 2) Fanta o 3) Sprite (validar opción). 
# Además, se debe pedir el dinero a pagar por la bebida.
# -	Si el dinero es igual a $400 no tiene vuelto.
# -	Si el dinero es mayor a $400 debe calcular y entregar vuelto.
# -	Si el dinero es menor a $400 debe mandar un mensaje de alerta y no entregar la bebida.
# Finalizado el proceso, esperar una nueva orden.

## agregar contadores para saber cuantas bebidas se vendieron de cada una. 
# Crear otra opcion en el menú


# Agregar opción total de ventas: Suma todas las ventas realizadas. Ocupar un acumulador

import os
opcion = ""
cocacola = 0
fanta = 0
sprite = 0
totalVentas = 0
fueVendida = False


while opcion != "6":
    os.system("cls")
    print("********  La Maquina ********")
    print("1.- Coca-Cola")
    print("2.- Fanta")
    print("3.- Sprite")
    print("4.- Contadores")
    print("5.- Total de ventas")
    print("6.- Salir")

    opcion = input("Ingrese una opción:")

    if opcion not in ("1", "2", "3", "4", "5", "6"):
        print("La opción no es válida")
    elif opcion == "4":
        print("**** R E P O R T E ****")
        print("CocaCola : ", cocacola)
        print("Fanta    : ", fanta)
        print("Sprite   : ", sprite)
        print("Total de bebidas: ", (cocacola+ fanta + sprite))
    elif opcion == "5":
        print("**** R E P O R T E ****")
        print("El total de ventas es : ", totalVentas)
    else:

        monto = int(input("Ingrese pago:"))

        vuelto = monto - 400

        if vuelto == 0:
            print("Gracias por su compra")
            fueVendida = True
        elif vuelto > 0:
            print("Gracias por su compra, su vuelto es $" + str(vuelto))
            fueVendida = True
        else:
            print("Falta dinero, vuelva a intentar")
            fueVendida = False
        
        if fueVendida:
            totalVentas += 400
            if opcion == "1":
                cocacola += 1
            elif opcion == "2":
                fanta += 1
            else:
                sprite += 1
    input("Presione enter para continuar")