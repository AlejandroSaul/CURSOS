#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando
# el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar 
# un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingrese el Primer Valor: "))
        self.num2 = int(input("Ingrese el Segundo Valor: "))
    
    def suma(self):
        self.suma = self.num1 + self.num2
        print( "La suma da como resultado: ",self.suma)
    
    def resta(self):
        self.resta = self.num1 - self.num2
        print("La resta da como resultado: ",self.resta)

    def multi(self):
        self.multi = self.num1 * self.num2
        return "La multiplicacion da como resultado: ",self.multi

    def division(self):
        self.division = self.num1 / self.num2
        return "La division da como resultado: ",self.division

calcular = Calculadora()
calcular.suma()
calcular.resta()
print(calcular.multi())
print(calcular.division())