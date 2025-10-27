#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

#[20, 50, "Curso", 'Python', 3.14]

lista = [20 , 50 , "Curso" , 'Python' , 3.14]
print("Estos son los valores actuales de la lista: ", lista)

palabra1 = input("Ingrese el primer valor para sustituir en el espacio 1: ")
palabra2 = input("Ingrese el segundo valor para sustituir en el espacio 2: ")

lista[0] = palabra1
lista[1] = palabra2

print("El nuevo valor de la lista es: {}".format(lista))