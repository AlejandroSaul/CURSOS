'''Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
años que ha cumplido (desde 1 hasta su edad).'''

edad = int(input('Digite su edad : '))
i = 1
while i<edad:
    print('Has cumplido {} años'.format(i))
    i += 1