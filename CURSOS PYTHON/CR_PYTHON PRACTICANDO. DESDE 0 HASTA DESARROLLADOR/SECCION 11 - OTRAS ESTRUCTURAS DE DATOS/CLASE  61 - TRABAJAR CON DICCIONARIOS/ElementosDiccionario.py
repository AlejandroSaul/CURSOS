diccionario = {'Nombre':"Walter",'Apellido':"Coto","Estatura":1.80}
print(diccionario.keys())
print(diccionario.values())

print(diccionario["Estatura"])
print(diccionario.get('Nombre'))

diccionario["Peso"] = "58 kg"

print(diccionario)