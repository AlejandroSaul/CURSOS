#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
# luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
# Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
# Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica ():
    def __init__(self,llantas,color,precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    
class Moto (Fabrica):
    def imprimir(self):
        print("La cantidad de llantas es {}".format(self.llantas))
        print("El color es {}".format(self.color))
        print("El precio es {}".format(self.precio))

class Auto (Fabrica):
    def imprimir(self):
        print("La cantidad de llantas es {}".format(self.llantas))
        print("El color es {}".format(self.color))
        print("El precio es {}".format(self.precio))

moto = Moto(2,'Rojo',2000)
auto = Auto(4,'Blanco',20000)

moto.imprimir()
auto.imprimir()