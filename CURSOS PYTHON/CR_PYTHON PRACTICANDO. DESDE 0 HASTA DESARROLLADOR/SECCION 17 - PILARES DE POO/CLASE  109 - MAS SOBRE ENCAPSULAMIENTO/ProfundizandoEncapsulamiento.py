class A():
    def __init__(self):
        # self.contador = 0
        # self.cuenta = 0
        self._contador = 0
        self._cuenta = 0
    
    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()
# print(a.cuenta)
# a.cuenta = 20
# print(a.cuenta)

