print("|====  Ingreso de datos  ====|")
nombre  = input("Nombre  : ")
rut     = input("Rut     : ")
email   = input("Email   : ")
telefono= input("Télefono: ")

print("Sus datos son:")
print("Nombre   : ", nombre )
print("Rut      : ", rut )
print("Email    : ", email )
print("Télefono : ", telefono )

print("\n")
print("Nombre   : ", nombre, "\nRut      : ", rut, "\nEmail    : ", email,"\nTélefono : ", telefono )
print("Nombre   : {} \nRut      : {} \nEmail    : {} \nTélefono : {}".format(nombre,rut, email, telefono) )

