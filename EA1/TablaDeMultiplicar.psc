Algoritmo TablaDeMultiplicar
	//Ingrese un numero > 0 y multiplicarlo
	// del 1 al 10
	Definir numero1 Como Entero
	Definir resutado Como Entero
	Escribir "*** Escriba número para la tabla ***"
	Leer numero1
	
	si numero1 < 1 Entonces
		Escribir "Debe ingresar un número positivo"
	SiNo
		Para contador <- 1 Hasta 10 Hacer
			resultado = numero1 * contador
			Escribir numero1, " X ", contador, " = ", resultado 
		FinPara
		Escribir "==== Fin Tabla de Multiplicar ===="
	FinSi
	
FinAlgoritmo
