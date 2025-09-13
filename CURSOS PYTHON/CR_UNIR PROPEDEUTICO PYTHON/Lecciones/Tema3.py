lista = [3,'Hola',True]
print(lista[:2])
print(lista[1:])
print(len(lista[1]))
lista.append([1,2])
print(lista)
lista[3]='Hola'
print(lista)
lista.remove('Hola')
print(lista)
lista = [1,2,3,4,6,10,9,8]
print(lista)
lista.sort()
print(lista)
lista.pop(7)
print(lista)
boleano = 6 in lista
print(boleano)

#-------------
"""Desempaquetado de tuplas"""
tupla = 1,2,3,4
w,x,y,z = tupla 


print(w)

diccionario = {'a':1,'b':2}
print(diccionario)
print(diccionario['a'])
del diccionario['a']
print(diccionario)

conjunto = {1,2,3,1}
print(conjunto)

#---

cadena = 'Hola'
iterador = iter(cadena)

print(next(iterador))
print(next(iterador))
print(next(iterador))