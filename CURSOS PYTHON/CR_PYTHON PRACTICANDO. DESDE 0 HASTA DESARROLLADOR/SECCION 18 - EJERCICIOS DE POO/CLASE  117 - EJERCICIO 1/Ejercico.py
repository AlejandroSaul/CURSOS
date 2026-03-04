'''
Ejercicio 1
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y 
la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje 
con el resultado de la nota y si ha aprobado o no.
'''

class Estudiante():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota 
    def rasultado(self):
        if self.nota > 6:
            aprobado = 'SI'
        else :
            aprobado = 'NO'

        print('El alumno {} tuvo la nota de {} por lo tanto {} fue aprobado'.format(self.nombre,self.nota,aprobado))

estudiante1 = Estudiante('Alejandro',10)

estudiante1.rasultado()
