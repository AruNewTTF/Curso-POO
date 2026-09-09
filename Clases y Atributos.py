class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")
    def cortar(self):
        print("Cortaste una llamada")
        
celu1 = Celular("Samsung", "S23", "48MP")

celu1.llamar()