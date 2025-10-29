'''
Ejercicio 1
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya
 ingresado, es el mes que debe mostrar en la tupla'''

meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

bandera = True
while bandera:
    try:
        mesElegido = int(input('Digite un numero de mes: '))
        print("El mes elegido es : {}".format(meses[mesElegido-1]))
        bandera = False
    except:
        print('Digita un número entre 1 y  12!!')