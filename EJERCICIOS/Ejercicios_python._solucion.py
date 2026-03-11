'''Ejercicio 1
Python Practicando. Desde 0 hasta Desarrollador en Python - Clase 26
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
• Imprima los dos primeros caracteres.
• Imprima los tres últimos caracteres.
• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.'''

cadena = "Te quiero solo como amigo"

print(cadena[0 : 2])
print(cadena[-3 : ])
print(cadena[: : 2])
print(cadena[: : -1])
print(cadena + cadena[: : -1])

'''Ejercicio 2
Python Practicando. Desde 0 hasta Desarrollador en Python - Clase 34
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final'''

P1 = float(input('Digite la calificacion de la practica 1: '))
P2 = float(input('Digite la calificacion de la practica 2: '))
P3 = float(input('Digite la calificacion de la practica 3: '))
EP = float(input('Digite la calificacion del examen parcial: '))
EF = float(input('Digite la calificacion del examen final: '))

PP = ( P1 + P2 +P3 ) / 3 
PROM = ( PP + 2*EP + 3*EF ) / 6
print(PP)

'''Ejercicio Extra
Python Practicando. Desde 0 hasta Desarrollador en Python - Clase 39
Combrobar si la cadena de texto:
cadena = "Estoy mostrando los metodos booleanos para las Strings"
empieza con 'E' (debe ser True)
termina con 's' (debe ser True)
se encuentra en mayusculas (debe ser False)
se encuentra en minusculas (debe ser False)
'''

cadena = "Estoy mostrando los metodos booleanos para las Strings"

print(cadena.startswith('E'))
print(cadena.endswith('s'))

print(cadena.isupper())
print(cadena.islower())

'''Ejercicio 2 (Modificado : Usar Funiones y Excepciones)
Python Practicando. Desde 0 hasta Desarrollador en Python - Clase 47
Escribir un programa que, dado un número entero, muestre su valor absoluto. 
Nota: para los números positivos su valor absoluto es igual al número 
(el valor absoluto de 52 es 52)
, mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 
(el valor absoluto de -52 es 52).'''

def esNumero(numero):
    try:
        numero = int(numero)
        return True
    except:
        return False
    
bandera = True
numero = input('Digite un numero entero: ')

while bandera:
    if esNumero(numero):
       bandera = False
    else:
        print('Lo digitado no es un numero entero')
        numero = input('Digite un numero entero: ')

numero = int(numero)    
if numero >= 0:
    print('Su valor absoluto es {}'.format(numero))
else:
    print('Su valor absoluto es {}'.format(numero*-1))
