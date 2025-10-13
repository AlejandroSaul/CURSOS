'''Ejercicio 1
Python Practicando. Desde 0 hasta Desarrollador en Python - Clase 48
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas
letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un
poco y si no, que no riman.'''
bandera = True
while bandera:
    palabra1 = input('Escriba la primera palabra: ')
    palabra2 = input('Escriba la segunda palabra: ')

    longitudP1 = len(palabra1)
    longitudP2 = len(palabra2)
    if longitudP1 >2 and longitudP2 >2:
        bandera = False
    else:
        print('Alguna de las palabras no tiene una longitud mayor a 3 caracteres')

ultimasTresP1 = palabra1[len(palabra1)-3::1].lower()
ultimasTresP2 = palabra2[len(palabra2)-3::1].lower()
ultimasDosP1 = palabra1[len(palabra1)-2::1].lower()
ultimasDosP2 = palabra2[len(palabra2)-2::1].lower()

if ultimasTresP1 == ultimasTresP2:
    print('Las palabras riman')
elif ultimasDosP1 == ultimasDosP2:
    print('Las palabras riman un poco')
else:
    print('No riman')