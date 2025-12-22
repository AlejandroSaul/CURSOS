class Animales():
    def __init__(self,nombre):
        self.nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre) #Para heredar del constructor del padre
        self.sonido = sonido

perro = Perro('Firulais','Guau')
print(perro.nombre)