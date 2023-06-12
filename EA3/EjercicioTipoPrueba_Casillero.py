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
    print("***** Registro de arriendo *****")
    print("1.- Casillero Super Grande $2.000")
    print("2.- Casillero Grande $1.000")
    print("3.- Casillero Pequeño $500")
    print("0.- Salir")
    casillero = input("Ingrese tipo de casillero: ")
    if casillero not in listaDeTiposCasilleros:
        print("La opción ingresada no es válida")
        input("Presione enter para continuar...")
    else:
        fila = int(casillero) # convertir de str a int. es la fila
        # mostrar casilleros disponibles ???
        casillerosDisponibles(casilleros, fila)

        # validar que la conversión sea exitosa
        try:
            nroCasillero = int(input("Ingrese nro del casillero: "))
            columna = nroCasillero -1 # matriz empieza con indice 0
            fila -= 1 # matriz empieza con indice 0
            rut = input("Ingrese su rut:")

            # almacena el rut en el casillero seleccionado
            casilleros[fila, columna] = rut

            # almacena y suma las ventas realizadas
            if fila == 0: # es por el indice cero de la matriz
                totalVentas += 2000
            elif fila == 1:
                totalVentas += 1000
            elif fila == 2:
                totalVentas += 500

            print("Datos guardados")
            input("Presione enter para continuar...")
        except: # si ingreso un casillero que no se puede convertir en número o no existe
            print("Error en la elección del casillero")
            input("Presione enter para continuar...")

def listarCasilleros(casilleros):
    pass
def totalDeVentas(casilleros):
    pass
def desocuparCasillero(casilleros):
    pass

def casillerosDisponibles(casilleros, fila):
    listado = ""
    nroCasillero = 1
    for columna in casilleros[fila-1]:
        if columna == "":
            listado += str(nroCasillero) + "\n"
        else:
            listado += "X" + "\n"
        nroCasillero+=1
    print(listado)


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




