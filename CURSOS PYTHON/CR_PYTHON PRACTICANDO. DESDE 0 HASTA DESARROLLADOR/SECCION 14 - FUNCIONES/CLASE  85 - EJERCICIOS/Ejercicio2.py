'''Ejercicio 2
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

def factorial(numero):
    resultado = 1
    for i in range(1,numero+1):
        resultado = resultado * i
    return resultado

print(factorial(5))