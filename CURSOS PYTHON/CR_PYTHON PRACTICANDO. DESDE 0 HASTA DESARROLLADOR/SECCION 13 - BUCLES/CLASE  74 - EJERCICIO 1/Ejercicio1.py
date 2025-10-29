#Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

numero = int(input("Ingresa un numero para saber su tabla: ")) #2
i = 0
multi = 0

while i <= 10:
    multi = numero * i #0
    print("{} x {} = {}".format(numero , i , multi))
    i += 1