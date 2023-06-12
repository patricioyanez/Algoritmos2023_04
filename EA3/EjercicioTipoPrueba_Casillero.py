# Crear una aplicación que permita registrar los arriendos de
# casilleros que tiene una empresa de turismo.
# Las categorias de estos casilleros son:
# 1.- Super Grande= $2000
# 2.- Grande      = $1000
# 3.- Pequeño     = $500
# 
# Los casilleros tienen una capacidad de 3 filas 
# (una para cada capacidad) y de 5 unidades para cada una
# Al arrendar uno, se debe registrar el rut
# 
# Las opciones a realizar son:

# 1.-Registro de arriendo
# 2.-Listar casilleros (ocupados y los que no)
# 3.-Totalizar la venta hasta el momento.
# 4.-Desocupar un casillero


# Usar funciones para cada una de las opciones
# validar que no esten vacios los datos a ingresar

import numpy as np
import os

# declarar variables
casilleros = np.array([ ["","","","",""],
                        ["","","","",""],
                        ["","","","",""],
                       ], dtype=object)

totalVentas = 0 # acumulador. Para sumar todas las ventas realizadas
filaCasillero = -1 # almacenará el tipo de casillero
columnaCasillero = -1 # almacenará el nro del casillero

listaDeOpcionesValidas = ["0","1","2","3","4"]
listaDeTiposCasilleros = ["1","2","3"]
opcion = ""
# declara las funciones para cada opción:
def registroDeArriendo(casilleros):
    pass
def listarCasilleros(casilleros):
    pass
def totalDeVentas(casilleros):
    pass
def desocuparCasillero(casilleros):
    pass

# definir el menú
while opcion != "0":
    os.system("cls")
    print("======= Administración de Casilleros ========")
    print("1.- Registro de arriendo")
    print("2.- Listar casilleros (ocupados y los que no)")
    print("3.- Total de ventas")
    print("4.- Desocupar casillero")
    print("0.- Salir")
    opcion = input("Seleccione una opción: ")

    #validar opción seleccionada
    if opcion not in listaDeOpcionesValidas:
        print("La opción ingresada no es válida")
        input("Presione enter para continuar...")
    elif opcion == "1":
        registroDeArriendo(casilleros)
    elif opcion == "2":
        listarCasilleros(casilleros)
    elif opcion == "3":
        totalDeVentas(casilleros)
    elif opcion == "4":
        desocuparCasillero(casilleros)




