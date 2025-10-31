#Escribir una función que reciba una muestra de números en una tupla y devuelva su medida.

def medida(*tupla):
    print(len(tupla))
    for i in tupla:
        print(i)
    print(type(tupla))
    return len(tupla)

print(medida(2 , 3 , 4 , 10 , 20))