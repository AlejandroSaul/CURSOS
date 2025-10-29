'''Ejercicio 1
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero'''

bandera = True
while bandera:
    try:
        numero = int(input('Digite un número entero : '))
        i = 0
        while i < 10 :
            i += 1
            print("{} x {} = {}".format(numero,i,numero * i))
        bandera = False    
    except:
        'El numero digitado no es un entero'