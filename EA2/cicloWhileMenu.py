opcion = ""

while opcion != "5":
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")
## ejercicios: agregar Multiplicación y división
    opcion = input("Ingrese una opción:")

    if opcion not in ("1", "2", "3", "4", "5"):
        print("La opción no es válida")
    elif opcion == "1":
        n1 = int(input("Ingrese 1er valor:"))
        n2 = int(input("Ingrese 2do valor:"))
        print("La suma es:", n1 + n2)
    elif opcion == "2":
        n1 = int(input("Ingrese 1er valor:"))
        n2 = int(input("Ingrese 2do valor:"))
        print("La resta es:", n1 - n2)
    elif opcion == "3":
        n1 = int(input("Ingrese 1er valor:"))
        n2 = int(input("Ingrese 2do valor:"))
        print("La multiplicación es:", n1 * n2)
    elif opcion == "4":
        n1 = int(input("Ingrese 1er valor:"))
        n2 = int(input("Ingrese 2do valor:"))

        if n2 == 0:
            print("No se puede dividir por cero")
        else:
            print("La división es:", n1 / n2)