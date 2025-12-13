class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property #con esto ya no tenemos que poner () al llamar al metodo lo toma como getter
    def cuenta(self):
        return self._cuenta
    
    @property #con esto ya no tenemos que poner () al llamar al metodo lo toma como getter
    def contador(self):
        return self._cuenta

a = A()
# print(a._cuenta)
print(a.cuenta)
print(a.contador)
# a._cuenta = 10
# print(a._cuenta)
