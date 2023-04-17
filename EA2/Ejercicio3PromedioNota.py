# Ingrese 3 notas por teclado (valide que sean entre 1 y 7) 
# y calcule su promedio. Si la nota resultante es 
# mayor o igual a 4.0 entonces indique que está aprobado, 
# en caso contrario notifique que está reprobado.

print("**** Promedio de notas ****")
nota1 = float(input("Ingrese primera nota: "))
nota2 = float(input("Ingrese segunda nota: "))
nota3 = float(input("Ingrese tercera nota: "))

if nota1 < 1 or nota1 > 7:
    print("La primera nota no es válida.")
elif nota2 < 1 or nota2 > 7:
    print("La segunda nota no es válida.")
elif nota3 < 1 or nota3 > 7:
    print("La tercera nota no es válida.")
else:
    # dentro del rango 1...7
    resultado = (nota1 + nota2 +nota3) / 3
    if resultado >= 4:
        print("Ud está aprobado")
    else:
        print("Ud. está reprobado, nos vemos en Enero :)")
