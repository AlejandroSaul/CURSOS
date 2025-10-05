'''Ejercicio 1
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”'''

a = float(input('Ingrese el número para a: '))
b = float(input('Ingrese el número para b: '))
c = float(input('Ingrese el número para c: '))

resultado1 = ((-b) + (((b**2)-(4*a*c))**.5))/2*a
resultado2 = ((-b) - (((b**2)-(4*a*c))**.5))/2*a

print('La solucion es : '+str(resultado1) + ' y ' + str(resultado2))