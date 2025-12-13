class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self,mensaje): #todo metodo de instancia lleva self
        return mensaje
    
    def escucharMusica(self):
        return 'Estas escuchando musica'

telefono = FabricaTelefonos()

print(telefono.marca)
print(telefono.llamar('Hola ¿con quién hablo?'))
print(telefono.escucharMusica())