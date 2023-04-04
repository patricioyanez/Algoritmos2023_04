Algoritmo EjercicioVotacion
	// existen 2 candidatos para la eleccion de 
	// consejeros.
	// crear un Algoritmo para contabilizar cada 
	// voto que obtenga cada consejero.
	// una opcion debe Mostrar la cantidad total de 
	// votos
	
	Definir candidato1 Como Entero
	Definir candidato2 Como Entero
	Definir votosNulos Como Entero
	Definir opcion Como Entero
	
	Mientras opcion <> 5 Hacer
		Escribir "***** Votación consejeros *****"
		Escribir "[1] Candidato Juan"
		Escribir "[2] Candidato Ana"
		Escribir "[3] Nulo"
		Escribir "[4] Reporte"
		Escribir "[5] Salir"
		Escribir "Seleccione opción"
		Leer opcion
		
		si opcion = 1 Entonces
			candidato1 = candidato1 + 1 
		FinSi
		si opcion = 2 Entonces
			candidato2 = candidato2 + 1 
		FinSi
		si opcion = 3 Entonces
			votosNulos = votosNulos + 1 
		FinSi
		
		si opcion = 4 Entonces
			totalVotos =  candidato1+candidato2+votosNulos
			p1= candidato1 * 100 / totalVotos
			p2= candidato2 * 100 / totalVotos
			vn= votosNulos * 100 / totalVotos
			Escribir "Reporte de votos"
			Escribir "candidato 1	: ", candidato1, " (", p1,"%)"
			Escribir "candidato 2	: ", candidato2, " (", p2,"%)"
			Escribir "Nulos			: ", votosNulos, " (", vn,"%)"
			Escribir "Total de votos: ", totalVotos
		FinSi
	FinMientras
	
	
FinAlgoritmo
