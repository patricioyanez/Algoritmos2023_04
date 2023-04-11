# if elif else

# Candidato 1, Candidato 2, Nulo/Blanco
print("Ingrese su voto:")
voto = input("[1] Candidato 1 [2] Candidato 2 [3] Nulo/Blanco")
# input devuelve un str (string)
voto = int(voto)

if voto == 1:
    print("Voto por el candidato 1")
elif voto == 2:
    print("Voto por el candidato 2")
elif voto == 3:
    print("Su voto es nulo o blanco")

if voto == 1:
    print("Voto por el candidato 1 (2)")
elif voto == 2:
    print("Voto por el candidato 2 (2)")
else:
    print("Su voto es nulo o blanco (2)")