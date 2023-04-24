print("Contar números menores a cero")
lado1 = int(input("ingrese 1er lado: "))
lado2 = int(input("ingrese 2do lado: "))
lado3 = int(input("ingrese 3er lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("Triángulo equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")