'''Ejercicio 2
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un 
número, el que haya ingresado, es la letra que debe imprimir el programa'''

alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

bandera  =  True

while bandera:
    try:
        numero = int(input('Digite un numero entre 1 y 27: '))
        print("La letra elegida es: {}".format(alfabeto[numero-1]))
        bandera = False
    except:
        print("No es un numero entre 1 y 27 intentelo nuevamente")