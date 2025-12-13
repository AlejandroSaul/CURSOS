class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property #con esto ya no tenemos que poner () al llamar al metodo lo toma como getter
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter
    def cuenta(self,cuenta):
        self._cuenta = cuenta

    @property #con esto ya no tenemos que poner () al llamar al metodo lo toma como getter
    def contador(self):
        return self._cuenta
    
    @contador.setter
    def contador(self, contador):
        self._contador = contador

a = A()
# print(a._cuenta)
print(a.cuenta)
# a._cuenta = 20
a.cuenta = 20
print(a.contador)
a.contador = 10
print(a.contador)
# a._cuenta = 10
# print(a._cuenta)
