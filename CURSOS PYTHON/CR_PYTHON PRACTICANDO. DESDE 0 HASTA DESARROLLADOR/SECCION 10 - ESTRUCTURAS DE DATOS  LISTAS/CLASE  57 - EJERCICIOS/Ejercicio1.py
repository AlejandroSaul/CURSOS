'''Ejercicios

Ejercicio 1
En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:
[20, 50, "Curso", 'Python', 3.14]'''

lista = [20, 50, "Curso", 'Python', 3.14]
print('La lista actual es :' , lista)

valor1 = input('Inserte el primer valor a sustituir: ')
valor2 = input('Inserte el segundo valor a sustituir: ')

lista.insert(0,valor1)
del lista[1]
lista.insert(1,valor2)
del lista[2]

print(lista)