Algoritmo Ejercicio2
	Definir numero1 Como Entero
	Definir numero2 Como Entero
	
	Escribir "Ingrese n�mero 1:"
	Leer numero1
	Escribir "Ingrese n�mero 2:"
	Leer numero2
	
	si numero1 > 0 y numero2 > 0 Entonces
		si numero1 > numero2 Entonces
			Escribir "El numero1 es mayor(",numero1,")"
		SiNo
			si numero1 = numero2 Entonces
				Escribir "Los numeros son iguales (", numero2, ")"
			sino	
				Escribir "El numero2 es mayor (", numero2, ")"
			FinSi
		FinSi
	SiNo
		Escribir "Solo se permite ingresar numeros positivos"
	FinSi
FinAlgoritmo