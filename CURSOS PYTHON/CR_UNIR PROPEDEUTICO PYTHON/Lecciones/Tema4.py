import math

#Argumentos por posición
#se deben definir los parámetros como una lista dinámica.
def imprime_numeros(*args):
    for numero in args:
        print(numero)

imprime_numeros(1,2,3,4)

#Argumentos por nombre
#para recibir varios argumentos por nombre, sin saber la cantidad, es necesario definir los parámetros como un diccionario dinámico
def imprime_valores(**args):
    for argumento in args:
        print(argumento, '=>', args[argumento])

imprime_valores(arg1='hola',arg2=[2,3,4])

#---
def ejemplo():
    return 10,'hola'

print(type(ejemplo()))

#Documentar funciones PEP8

def potencia(base,exponente):
    """
    Función que calcula la potencia de dos numeros.
    Argumentos:
    base -- base de la operación
    exponente -- exponente de la operacion
    """
    return base ** exponente

# help(potencia)

#Funciones aritmeticas
#esta función devuelve el valor absoluto del valor x.
print(math.fabs(-1234))
#esta función devuelve el máximo común divisor de dos valores x e y
print(math.gcd(34,82))

#Funciones anonimas
"""def cuadrado(x):
    resultado = x ** 2
    return resultado"""#funcion normal

cuadrado = lambda x:x**2 #funcion lambda

print(cuadrado(8))

#Ejemplo de listas
lista = [1,2,3,4,5,6,7]

es_par = lambda numero:numero%2 ==0

print(list(filter(es_par,lista)))

# Aplicamos el filtro para obtener los números pares. Tenemos que insertarlo en una lista para tener el resultado en formato lista. 
print(list(map(cuadrado,lista)))