# Este codigo ha sido generado por el modulo psexport 20230113-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print("Ingresa tres numemros")
	a = input()
	b = input()
	c = input()
	if a>b:
		mayor = a
		menor = b
	else:
		mayor = b
		menor = a
	if mayor>c:
		if menor>c:
			menor = c
			print("El mayor es:",mayor)
			print("El menor es:",menor)
		else:
			print("El mayor es:",mayor)
			print("El menor es:",menor)
	else:
		mayor = c
		print("El mayor es:",mayor)
		print("El menor es:",menor)

