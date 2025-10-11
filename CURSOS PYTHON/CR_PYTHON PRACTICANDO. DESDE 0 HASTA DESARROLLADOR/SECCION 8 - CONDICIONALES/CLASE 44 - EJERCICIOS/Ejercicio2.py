'''Ejercicio 2
Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).'''
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

