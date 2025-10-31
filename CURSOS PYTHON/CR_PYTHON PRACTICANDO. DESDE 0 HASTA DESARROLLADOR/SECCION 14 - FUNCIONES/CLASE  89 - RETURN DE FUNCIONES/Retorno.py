import random
def entero ():
    print('Este es un dato entero')
    return random.randint(1,10)

def decimal ():
    print('Este es un dato decimal: ')
    return random.random()

def frase():
    return("Mi nombre es ")

def asignacion():
    return 1,2,3,4,5

print(entero())
print(decimal())
print(frase)

a,b,c,d,e = asignacion()

print(a)
print(b)