# Solicitar edad y clasifiquelo según rango etario
# niño, adolescente, adulto, adulto mayor

print("|=== Clasificación etaria ===|")
edad = input("Ingrese su edad:") # str (string)
edad = int(edad)  # convierte el str en int

if edad <= 12:
    print("Ud es un niño")
elif edad < 19:
    print("Ud es un adolescente")
elif edad < 65:
    print("Ud es un adulto")
else:
    print("Ud es adulto mayor")