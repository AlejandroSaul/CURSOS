#Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

tupla = ('enero' , 'febrero' , 'marzo' , 'abril' , 'mayo' , 'junio' , 'julio' , 'agosto' , 'septiembre' , 'octubre' , 'noviembre' , 'diciembre')

OpcionMes = int(input("Ingresa el numero de tu mes: "))

print("El mes correspondiente es: ", tupla[OpcionMes-1])