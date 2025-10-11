'''Ejercicio 1
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". 
Sino, decirle al usuario que no es vocal'''
vocales = ['a','e','i','o','u']
letra = input('Escribe una letra: ')
if letra.lower() in vocales:
    print('Es vocal')
else:
    print('No es vocal')

