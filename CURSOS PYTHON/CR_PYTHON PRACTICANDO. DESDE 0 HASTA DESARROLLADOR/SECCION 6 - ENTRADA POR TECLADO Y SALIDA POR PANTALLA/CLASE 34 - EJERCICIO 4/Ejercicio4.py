#Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

#Te llamas: <nombre>

#Tu edad es: <edad>

#Eres: <sexo>

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
sexo = input("Ingresa tu sexo: ")

print("Te llamas: {}\nTu edad es: {}\nEres: {}".format(nombre,edad,sexo))