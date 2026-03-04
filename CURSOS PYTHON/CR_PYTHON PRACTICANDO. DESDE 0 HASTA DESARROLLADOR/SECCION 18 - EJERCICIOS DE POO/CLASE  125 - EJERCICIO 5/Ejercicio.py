'''Ejercicio 1

Crear un programa con tres clases Universidad, con atributos nombre 
(Donde se almacena el nombre de la Universidad). Otra llamada Carerra, 
con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto
llamado persona.'''

class Universidad():
    def __init__(self,nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

class Carrera():
    def __init__(self,especialidad):
        self._especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad

class Estudiante():
    def __init__(self,nombre,edad,universidad,carrera):
        self._nombre = nombre
        self._edad = edad
        self._universidad = universidad
        self._carrera = carrera
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def universidad(self):
        return self._universidad
    
    @property
    def carrera(self):
        return self._carrera

universidad = Universidad("UVM")
carrera = Carrera("Ing. de Software")
estudiante = Estudiante("Saul","33",universidad,carrera)

print("Hola soy {} tengo {} años, estudie en la univaridad {} la carrera de {}".format(
    estudiante.nombre,
    estudiante.edad,
    estudiante.universidad.nombre,
    estudiante.carrera.especialidad))