'''Ejercicio 2.1. Elaborar algoritmo y programa en Python para determinar la temperatura en 
grados Farenheit y Kelvin si se proporciona en grados centigrados (Un dato de entrada y 
dos salidas).'''

celsuis = float(input("Digite los grados centigrados: "))

Fahrenheit = (celsuis * 1.8) + 32

Kelvin = celsuis + 273.15



print("Fahrenheit = ", Fahrenheit)

print("Kelvin = ",Kelvin)



