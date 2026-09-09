class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
celu1 = Celular("Samsung", "S23", "48MP")

print(celu1.modelo)