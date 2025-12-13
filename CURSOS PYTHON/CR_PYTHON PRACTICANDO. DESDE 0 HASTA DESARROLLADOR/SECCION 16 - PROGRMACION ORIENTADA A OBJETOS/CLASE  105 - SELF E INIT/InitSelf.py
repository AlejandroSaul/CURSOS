# class FabricaTelefonos():
#     marca = "Samsung"

#     def ElaborarHuawei(self):
#         self.marca = "Huawei"

# telefono = FabricaTelefonos()
# print(telefono.marca)
# telefono.ElaborarHuawei()
# print(telefono.marca)

class FabricaTelefonos():
    # def __init__(self):
    #     print("Estoy ejecutando el metodo init porque se a creado un nuevo objeto")
    #     pass
    def __init__(self,marca, color):
        print("La marca es {} y el color es {}".format(marca,color))
        pass

# telefono = FabricaTelefonos()
telefono2 = FabricaTelefonos('Samsung','Negro')


