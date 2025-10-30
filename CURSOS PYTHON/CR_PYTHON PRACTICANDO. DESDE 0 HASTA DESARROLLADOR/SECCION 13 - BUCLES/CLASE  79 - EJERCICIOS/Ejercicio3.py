'''Ejercicio 2

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2
números, pero, solo imprimiendo los números que sean impares'''

bandera = True
while bandera:
    try:
        numero = int(input('Digite un numero entero : '))
        numero2 = int(input('Digite otro numero entero : '))
        print('Los numeros impares entre este rango de numeros es :')
        if(numero>numero2):            
            for i in range(numero2,numero):
                if i%2 != 0:
                    print("{} es impar".format(i))
        else:
            for i in range(numero,numero2):
                if i%2 != 0:
                    print("{} es impar".format(i))
        bandera = False
    except:
        print('Los datos introducidos no son correctos revisalos nuevamente')