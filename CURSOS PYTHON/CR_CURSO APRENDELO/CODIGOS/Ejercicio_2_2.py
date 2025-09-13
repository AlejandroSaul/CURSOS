"""Ejercicio 2.2. Elaborar algoritmo y programa en Python para determinar conversiones (peso, 
distancia, divisas, etc.) (Un dato de entrada y varias salidas)."""

print("Digite el tipo de dato a convertir: ")
print("1.- Peso")
print("2.- Distancia")
print("3.- Divisa")

eleccion = int(input())

if eleccion == 1 :
    kilogramos =float(input("Digite los kilogramos : "))
    gramos = kilogramos*1000
    print(f"Los gramos son : {gramos}")
elif eleccion == 2:
    kilometros = float(input("Digite Kilometros : "))
    metros = kilometros*1000
    print(f"Los metros son : {metros}")
else:
    pesos = float(input("Digite los pesos : "))
    dolares = pesos / 18
    print(f"Los dolares son : {dolares}")
