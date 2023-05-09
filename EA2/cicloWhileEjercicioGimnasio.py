# En un Gimnasio se está realizando una encuesta para determinar la cantidad de 
# personas según el rango etario que asisten a él. Existen tres rangos o categorías:

# -	Entre 10 y 17 años niño.
# -	Entre 18 y 29 años joven.
# -	Entre 30 y 50 años adulto.
# 
# Las personas que asisten al gimnasio deben estar entre estos rangos de edad.
# Desarrolle un programa que permita determinar:
# 
# -	El promedio de edad de las personas que asisten al gimnasio.
# -	La cantidad de mujeres y hombres que asisten al gimnasio.
# -	La cantidad final por categoría (rango etarios)
# 
# El programa debe solicitar por pantalla el sexo (F ó M) y la edad de la 
# persona (validar datos de entrada).
# 
import os
opcion = ""
# contadores
nino = 0
joven= 0
adulto= 0
femenino = 0
masculino= 0
cantidadEdades =0

#acumulador
sumaEdades = 0

while opcion != "5":
    os.system("cls")
    print("********  Encuesta gimnasio ********")
    print("1.- Ingreso de datos")
    print("2.- Reporte Promedio edad")
    print("3.- Reporte cantidad de mujeres y hombres")
    print("4.- Reporte cantidad rango etario")
    print("5.- Salir")
    opcion = input("Ingrese una opción:")

    if opcion not in ("1", "2", "3", "4", "5"):
        print("La opción no es válida")
    elif opcion == "1":
        edad = int(input("Ingrese su edad")) # se asume que se ingresará un numero
        sexo = input("Ingrese sexo F:femenino y M:masculino")

        ## validar
        if edad < 10 or edad > 50:
            print("Edad fuera del rango aceptado")
        elif sexo not in ("F", "f", "M", "m"):
            print("Opción no es valida")
        else:
            # valores permitidos

            if edad <= 17:
                nino = nino + 1
            elif edad <= 29:
                joven = joven + 1
            else:
                adulto += 1

            if sexo.upper() == "F":
                femenino += 1
            else:
                masculino += 1

            sumaEdades += edad
            cantidadEdades +=1
    elif opcion == "2":
        print("===== Promedio de edades =====")
        print("El promedio de edad es:" , (sumaEdades/cantidadEdades))
    elif opcion == "3":
        print("===== Reporte cantidad de mujeres y hombres =====")
        print("Cantidad de sexo masculino: ", masculino)
        print("Cantidad de sexo femenino: ", femenino)
    elif opcion == "4":
        print("===== Reporte cantidad rango etario =====")
        print("Cantidad de edad joven: ", joven)
        print("Cantidad de edad nino: ", nino)
        print("Cantidad de edad adulto: ", adulto)
        
