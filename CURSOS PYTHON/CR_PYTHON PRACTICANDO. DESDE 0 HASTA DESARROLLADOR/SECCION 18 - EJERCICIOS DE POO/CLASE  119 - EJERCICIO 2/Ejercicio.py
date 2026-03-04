#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando 
# el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar 
# un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class calculadora():
    def __init__(self,valorUno,valorDos):
        self.valorUno = valorUno
        self.valorDos  = valorDos 

    def calculos(self):
        try:              
            suma = self.valorUno + self.valorDos
            resta = self.valorUno - self.valorDos
            multiplicaicon = self.valorUno * self.valorDos
            print("La suma es : {}".format(suma))
            print("La resta es : {}".format(resta))
            print("La multiplicacion es : {}".format(multiplicaicon))
        except:
            print("El valor 1 debe ser un numero")

        try:
                    division = self.valorUno / self.valorDos
                    print("La division es : {}".format(division))
        except:
              print("El valor 1 debe ser un numero y no puede ser 0")
valorUno = float(input("Digite el valor 1: "))
valorDos = float(input("Digite el valor 2: "))
maquina = calculadora(valorUno,valorDos)
maquina.calculos()