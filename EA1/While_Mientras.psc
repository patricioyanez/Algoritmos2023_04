Algoritmo While_Mientras
	Definir valor Como Entero
	Mientras valor < 10 Hacer
		valor = valor + 1 // contador
		Escribir "El valor es:", valor
	FinMientras
	
	Definir opcion Como entero
	Mientras opcion <> 5 Hacer // ! =
		Escribir " ****** Menú Principal ******"
		Escribir "[1] Sumar"  
		Escribir "[2] Restar"  
		Escribir "[3] Multiplicar"  
		Escribir "[4] Dividir"  
		Escribir "[5] Salir"  
		Escribir "Seleccione opcion:"
		Leer opcion
		
		si opcion = 1 Entonces
			Escribir "Ingrese 1er nro:"
			Leer nro1
			Escribir "Ingrese 2do nro:"
			Leer nro2
			Escribir "El total es: ", nro1 + nro2
			Escribir "Precione cualquier tecla para continuar"
			Esperar Tecla
		FinSi
		si opcion = 2 Entonces
			Escribir "Ingrese 1er nro:"
			Leer nro1
			Escribir "Ingrese 2do nro:"
			Leer nro2
			Escribir "El total es: ", nro1 - nro2
			Escribir "Precione cualquier tecla para continuar"
			Esperar Tecla
		FinSi
		si opcion = 3 Entonces
			Escribir "Ingrese 1er nro:"
			Leer nro1
			Escribir "Ingrese 2do nro:"
			Leer nro2
			Escribir "El total es: ", nro1 * nro2
			Escribir "Precione cualquier tecla para continuar"
			Esperar Tecla
		FinSi
		si opcion = 4 Entonces
			Escribir "Ingrese 1er nro:"
			Leer nro1
			Escribir "Ingrese 2do nro:"
			Leer nro2
			
			si nro2 = 0 Entonces
				Escribir "No se puede dividir por cero"
			SiNo
				Escribir "El total es: ", nro1 / nro2
			FinSi
			Escribir "Precione cualquier tecla para continuar"
			Esperar Tecla
		FinSi
	FinMientras
	
	
	
FinAlgoritmo
