'''Ejercicio 1
Completa la siguiente función para que dado un número de documento nacional de identidad (DNI), se devuelva una letra. Esta letra se obtiene calculando el resto del DNI entre 23 y a partir de ese valor asignarle una letra de la siguiente tabla:
Tabla letras de control DNI
El valor DNI será un número entero y la letra debe ser una cadena de carateres que contendrá una única letra en mayúsculas.'''

def ejercicio_1(dni):
    # Escribe aquí el código del ejercicio
    resto = dni%23
    diccionario = {
        0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X', 11: 'B',
        12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'
    }
    letra = diccionario.get(resto)
    return letra

print(ejercicio_1(12))

'''Ejercicio 2
Completa la siguiente función para que dado el precio de un producto, se calcule y se
 devuelva el precio total que debe pagar el cliente, es decir, incluyenfo el IVA 
 (21% sobre el precio del producto). El precio total deberá ser únicamente el valor del
   precio, es decir, no debe contener el símbolo de la moneda. Redondee la salida al 
   segundo decimal en caso necesario.'''

def ejercicio_2(precio):
    # Escribe aquí el código del ejercicio
    precio_total = round(precio * 1.21,2)    
    return precio_total

'''Ejercicio 3
Completa la siguiente función para que dado el diámetro de una circunferencia, 
se calcule el área del círculo que contiene dicha circunferencia. Como valor de 
PI se usará  3.1415.'''
import math
def ejercicio_3(diametro):
    # Escribe aquí el código del ejercicio
    area = math.pow(diametro/2,2)* 3.1415
    return area

print(ejercicio_3(10))

'''Ejercicio 4
Completar la función para que dado dos números entéros y dos números enteros, 
se calcula el cociente y el resto de hacer la división entera entre n y m.'''
import math
def ejercicio_4(n, m):
    # Escribe tu programa aquí
    cociente = round(math.floor(n / m))
    resto = n % m
    return cociente, resto

print(ejercicio_4(234,5))

'''Ejercicio 5
Completar la función para que dado el número de unidades que ha comprado un usuario de 
2 productos diferentes, devolver el peso total del paquete para enviar su compra por
 mensajería. El peso de cada unidad del producto1 es de 147 unidades y el peso de cada 
 unidad del producto2 es de 2400 unidades. La función debe devolver únicamente el peso 
 total.
 '''

def ejercicio_5(producto1, producto2):
    # Escribe tu programa aquí
    pesoA= producto1 * 147
    pesoB = producto2 * 2400
    peso_total = pesoA + pesoB 
    return peso_total