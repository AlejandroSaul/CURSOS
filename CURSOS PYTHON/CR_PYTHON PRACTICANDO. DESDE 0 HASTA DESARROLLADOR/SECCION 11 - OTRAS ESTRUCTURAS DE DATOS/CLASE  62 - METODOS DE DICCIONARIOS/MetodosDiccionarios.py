diccionario = {1:2,2:3,3:4}
print(diccionario)
diccionario.pop(3)
print(diccionario)
diccionario.clear()
print(diccionario)

diccionario = {1:2,2:3,3:4}

print(diccionario.get(2))

diccionario.setdefault(4,5)

print(diccionario)

diccionario2 = { 4:5, 5:6, 6:7}

diccionario.update(diccionario2)
diccionario2 = diccionario.copy()
print(diccionario2)