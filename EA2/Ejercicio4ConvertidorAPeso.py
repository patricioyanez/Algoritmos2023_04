# Genere un convertidor de: 
# Ingrese un monto en $ para convertirlo a:
# Dólar a pesos chilenos 
# Peso Argentino a peso chileno 
# Yen a pesos chilenos 
# 
# Buscar los valores de hoy

print("*** Convertior a Pesos Chileno ***")
usd = 801
arg = .27
yen = .16
valorMoneda = 0.0
monto = float(input("Ingrese monto de la moneda:"))
moneda= input("Seleccione moneda [1]USD [2] ARG [3]Yen:")

if moneda == "1":
    valorMoneda = usd
elif moneda == "2":
    valorMoneda = arg
else:
    valorMoneda = yen

total = valorMoneda * monto
print("El total en pesos CL es: $", int(total))