'''Ejercicio 1
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio'''
import math
def area(*datos):
    if len(datos) == 1:
        area = (math.pi*math.pow(datos[0],2)) 
        print("El area del circulo es igual a : {}".format(area))
    elif len(datos) == 2 :
        area = datos[0] * datos[1]
        print("El area del rectangulo es igual a : {}".format(area))
    else : 
        print("No se pudo identificar la forma")

area(8)