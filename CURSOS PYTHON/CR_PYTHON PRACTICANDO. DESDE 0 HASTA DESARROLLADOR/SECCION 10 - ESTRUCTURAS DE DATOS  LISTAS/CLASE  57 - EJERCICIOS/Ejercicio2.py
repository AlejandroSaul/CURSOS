'''Ejercicio 2
Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos'''
lista = []
for i in range (1,11):
    lista.append(i)

print(lista)

lista.insert(4,lista[4]*2)
del lista[5]
lista.insert(7,lista[7]*2)
del lista[8]
lista.insert(9,lista[9]*2)
del lista[10]

print(lista)