class Animales():
    def __init__(self,mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print('Soy un perro')

class Pez(Animales):
    def hablar(self):
        print('Soy un pez')

perro = Perro("")

perro.hablar()

animal = Animales("Miau")

animal.hablar()