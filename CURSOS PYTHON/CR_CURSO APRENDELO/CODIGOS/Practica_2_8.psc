Algoritmo Encuentra_mayor
	Escribir "Ingresa tres numemros"
	Leer A,B,C
	Si A>B Entonces
		mayor = A
		menor = B
	SiNo
		mayor = B
		menor = A
	Fin Si
	
	Si mayor>C Entonces
		Si menor>C Entonces
			menor = C
			Escribir "El mayor es:" mayor
			Escribir "El menor es:" menor
		SiNo
			Escribir "El mayor es:" mayor
			Escribir "El menor es:" menor
		Fin Si
	SiNo
		mayor = C
		Escribir "El mayor es:" mayor
		Escribir "El menor es:" menor
	Fin Si
FinAlgoritmo
