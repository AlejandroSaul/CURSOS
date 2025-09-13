'''Práctica 2.1. Elaborar algoritmo y programa en Python para calcular la fuerza de atracción de
dos cuerpos si se sabe que su fórmula es F = G * (masa1 * masa2) / distancia ^2. Esta
práctica tiene varios datos de entrada y produce una salida.'''


G = 9.81
masa1 = float(input("Digite masa 1:"))
masa2 = float(input("Digite masa 2:"))
distancia = float(input("Digite distancia:"))


F = G * (masa1*masa2)/(distancia*distancia)

print("La Fuerza es: ",F)