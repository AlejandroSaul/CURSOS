'''Ejercicio 1
Escribe una clase llamada Numero. Esta clase debe tener una constructora que reciba un número y 
almacene ese número en 2 atributos: romano que almacenará el número en el formato de número romanos 
como una cadena de caracteres y normal que guardará el número que nos han dado en la constructora.'''
'''Ejercicio 2
Crea dos nuevos métodos en la clase Numero. El primer método, llamado imprime() imprime un mensaje 
mostrando el valor de ambos atributos; el segundo atributo, suma_romano() tendrá como parámetros una 
cadena de caracteres que representará otro número romano y que sumaremos a los atributos que ya teníamos.'''

'''Ejercicio 3
Define una función dentro de la clase Numero que a partir de una cadena de caracteres, devuelve True si esa 
cadena de caracteres corresponde con un número romano y falso en caso contrario. Después, modifica el método 
para que lance un error en el caso de que el valor que nos pasan por parámetro no se corresponde con el patrón 
de un número romano'''

class Numero:
    
    def __init__(self,numero):
        self.normal = numero
        self.romano = self.getRomano(numero)

    def getRomano(self,numero):
        romano = ''
        diccionario = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for numeros,valor in diccionario:
            while numero>=numeros:
                romano+=valor
                numero-=numeros
        return romano
    
    def imprime (self):
        print(self.normal,self.romano)

    def suma_romano(self,cadena):
        boleano = self.is_romano(cadena)
        if boleano == True:            
            suma_romana = self.normal + self.romano2Arabigo(cadena)
        else:
            raise Exception ('Error de dato')
        self.romano = self.getRomano(suma_romana)
        return suma_romana
    
    def is_romano(self,cadena):
        bandera = 1
        diccionario = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}
        if type(cadena) != str:
            bandera = 0
        else:
            for i in cadena:
                if i not in diccionario:
                    bandera = 0
        if bandera == 0:
            boleano = False
        else:
            boleano = True
        return boleano
    
    def romano2Arabigo(self,romano):
        diccionario = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
        totalCadena = 0            
        anterior = 0
        for letra in romano[::-1]:            
            valor = diccionario[letra]
            if valor < anterior:
                totalCadena -= valor
            else:
                totalCadena += valor
            anterior = valor
        return totalCadena

'''Ejercicio 4
Implementa una clase MejorNumero. Esta clase heredará las propiedades de Numero e incluirá dos métodos nuevos
 para restar y multiplicar los atributos recibiendo por parámetro otro número romano.''' 
 
class MejorNumero (Numero):
    def resta(self,numeroRomano):
        boleano = self.is_romano(numeroRomano)
        if boleano == True:            
            resta_romana = self.normal - self.romano2Arabigo(numeroRomano)
        else:
            raise Exception ('Error de dato')
        self.romano = self.getRomano(resta_romana)
        return self.romano
    
    def multiplica(self,numeroRomano):
        boleano = self.is_romano(numeroRomano)
        if boleano == True:            
            multiplicacion_romana = self.romano2Arabigo(numeroRomano) * self.romano2Arabigo(numeroRomano)
        else:
            raise Exception ('Error de dato')
        self.romano = self.getRomano(multiplicacion_romana)
        return self.romano
    
    def iterar(self,listaRomanos):
        total = self.normal
           
        for i in listaRomanos:
            boleano = self.is_romano(i)
            if boleano ==True:
                total += self.romano2Arabigo(i)
            else:
                print('Ha fallado el número '+ str(i))
        self.romano = self.getRomano(total)
        return self.romano

'''Ejercicio 5
En la clase MejorNumero, crea un nuevo método que reciba una lista con 3 números romanos. A continuación, 
iterando sobre los elementos de la lista llamará a la función suma_romano(). Los posibles errores se tendrán 
que gestionar con excepciones para mostrar un mensaje y seguir ejecutando el siguiente número.'''

aux = MejorNumero(29)
# aux.resta('XX')
# print(aux.romano)
# aux.multiplica('IX')
# print(aux.romano)
aux.iterar(['XX',675,'VI']) #Ha fallado el número 675 , LV
print(aux.romano)