Algoritmo ejercicio1A
	// Solicitar n cantidad de notas al usuario
	// promediarlas y entregar resultado (aprobado o no)
	// las notas deben estar en el rango de 10 a 70
	Definir cantidadNotas Como Entero
	Definir nota Como Entero
	Definir resultado Como Real
	Escribir "**** Promediador de notas ****"
	Escribir "Ingrese cantidad de notas: "
	Leer cantidadNotas
	
	Para indice <- 1 Hasta cantidadNotas Hacer
		Escribir "Ingrese nota nro ", indice, ": "
		Leer nota
		resultado = nota + resultado // acumulador
	FinPara
	resultado = resultado / cantidadNotas
	Escribir "Su promedio es: ", resultado
	
	si resultado >= 40 Entonces
		Escribir "Ud está Aprobado. Felicidades"
	SiNo
		Escribir "Ud. Reprobó. Lo espero en verano :)"
	FinSi
	
FinAlgoritmo
