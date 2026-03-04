'''Ejercicio 1

Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga 
"Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por 
"Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo 
llamado mensaje y que muestre ese mesjae como parametro'''

class Marino():
    def __init__(self):
        pass
    def hablar(self):
        print("Hola")

class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo")

class Foca(Marino):
    def __init__(self,mensaje):
        self.mensaje = mensaje
    def impMensaje(self):
        print(self.mensaje)

marino = Marino()
pulpo = Pulpo()
foca = Foca("Este es el mensaje")

marino.hablar()
pulpo.hablar()
foca.impMensaje()