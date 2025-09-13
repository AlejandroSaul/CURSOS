'''Ejercicio 1
Escribe una función llamada ejercicio1 que genere una lista con 15 valores enteros 
aleatorios que vayan de 1 a 100. La función debe devolver la lista con todos los valores.'''
import random
def ejercicio1():
    lista = []
    for i in range(15):
        lista.append(random.randint(1,100))
    return lista

'''Ejercicio 2
Escribe una función llamada ejercicio2 que recibe 2 argumentos: el primero será la 
lista que hemos implementado en el Ejercicio 1 y el segundo un número por el que se
 dividirá cada uno de los elementos de la lista. El resultado será una nueva lista.'''
lista = ejercicio1()
def ejercicio2(lista,numero):
    listaNueva = []
    for i in lista:
        listaNueva.append(i/numero)
    return listaNueva

''' Ejercicio 3
Usando funciones anónimas, crea una nueva lista que contenga los valores enteros de cada 
uno de los elementos de la lista que devuelve la función implementada en el Ejercicio 2.'''
import math
def ejercicio3(lista):
    resultado = []
    for i in lista:
        resultado.append(math.floor(i))
    return resultado

'''Ejercicio 4
Implementa una función, llamada ejercicio4, que reciba como argumentos dos números enteros y devuelva en una 
tupla los siguientes valores: el factorial del primer argumento y el máximo común divisor de ambos argumentos.'''

def ejercicio4(entero1,entero2):
    factorial = math.factorial(entero1)
    maximoDiv = math.gcd(entero1,entero2)
    tupla = (factorial,maximoDiv)
    return tupla

'''Ejercicio 5
Crea una función ejercicio5 que devuelva una lista con todos los valores contenidos en una lista que se pasa por 
argumento pero eliminando los valores repetidos. Prueba el funcionamiento de esta función con la lista obtenida 
en el Ejercicio 1.'''

def ejercicio5(lista):
    listaUnica=[]
    for i in lista:
        if i not in listaUnica:
            listaUnica.append(i)
    return listaUnica