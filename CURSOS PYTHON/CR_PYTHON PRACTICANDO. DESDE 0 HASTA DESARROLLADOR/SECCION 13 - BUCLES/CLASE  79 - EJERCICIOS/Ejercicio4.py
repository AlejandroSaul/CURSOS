'''Ejercicios
Ejercicio 1

Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y
mostrar el rango de numeros entre ambas cifras
'''

lista = []

for i in range(1,11):
    lista.append(i)

print(lista)
bandera = True
while bandera:
    try:
        numero = int(input('Digite un número entre 1 y 10: '))
        numero2 = int(input('Digite otro entre 1 y 10: '))
        if numero < 10 and numero >= 1 and numero2 < 10 and numero2 >= 1:
            if numero>numero2:
                print('El rango de numeros es: ')
                for i in range(numero2,numero+1):
                    print(i)
            else:
                print('El rango de numeros es: ')
                for i in range(numero,numero2+1):
                    print(i)
            bandera = False
    except:
        print('El rango de numeros no esta entre 1 y 10')
