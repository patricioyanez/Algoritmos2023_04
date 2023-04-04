Algoritmo Factorial
	// solicitar un numero y mostrar su factorial
	//EJ: 5 => 120
	Definir numero1 Como Entero
	Definir producto Como Entero
	Escribir "Ingrese número: "
	Leer numero1
	producto = 1
	Para contador <- 2 Hasta numero1 Hacer
		producto = producto * contador // contador y acumulador
	FinPara
	
	Escribir "El factorial de ", numero1, " es:", producto
FinAlgoritmo
