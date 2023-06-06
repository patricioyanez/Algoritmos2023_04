# crear una calculadora usando: menú, if, funciones, entre otros
# para las operaciones + - * / 
# considerar solo 2 números
def sumar(num1, num2):
    return num1 + num2
def restar(num1, num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero."
    return num1 / num2
# TAREA: agregar la sumatoria y factorial para un numero dado por el usuario
import os
opcion = ""
while opcion != "0":
    os.system("cls")
    print("=== Calculadora ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    opcion = input("Ingrese una opción:")

    if opcion not in("1","2","3","4","0"):
        print("Opción no válida")
        input("Presione enter para continuar...")
    else:    
        print("\nIngrese 2 números")
        num1 = int(input("Ingrese primer número: "))
        num2 = int(input("Ingrese segundo número: "))
        resultado = 0
        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)

        print("El resultado es:", resultado)
        input("Presione enter para continuar...")






        