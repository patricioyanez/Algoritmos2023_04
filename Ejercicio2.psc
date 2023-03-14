Algoritmo Ejercicio2
	Definir numero1 Como Entero
	Definir numero2 Como Entero
	
	Escribir "Ingrese número 1:"
	Leer numero1
	Escribir "Ingrese número 2:"
	Leer numero2
	
	si numero1 > 0 y numero2 > 0 Entonces
		si numero1 > numero2 Entonces
			Escribir "El numero1 es mayor(",numero1,")"
		SiNo
			Escribir "El numero2 es mayor o es igual al numero 1 (", numero2, ")"
		FinSi
	SiNo
		Escribir "Solo se permite ingresar numeros positivos"
	FinSi
FinAlgoritmo
