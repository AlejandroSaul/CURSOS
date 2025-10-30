'''Ejercicio 1

Crear un programa que tenga una lista, luego crear una funcion con la cual se van a 
pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en 
donde se ordenen los numeros pares e impares dentro de dos listas nuevas
'''
def agregar ():
    lista = []
    bandera = True
    while bandera :
        try:
            numero = input('Digite un numero a agregar a la lista o presione "s" para salir: ')
            if(numero == 's' or numero == 'S'):
                bandera = False
                return lista
            else:
                numero = int(numero)
                lista.append(numero)
        except:
            print('Lo digitado no es un numero entero válido, no se agrego a la lista')

def ordenar():
    lista = agregar()
    listaPares = []
    listaImpares = []
    for i in lista:
        if i%2 == 0:
            listaPares.append(i)
        else:
            listaImpares.append(i)
    print("Lista de pares {}".format(listaPares))
    print("Lista de impares {}".format(listaImpares))
ordenar()
