class Estudiante():
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando!")
        
Estudiante0 = Estudiante("Pipe",21,"Congelado")
Estudiante0.estudiar()

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
grado = input("Ingrese su grado: ")

Estudiante1 = Estudiante(nombre,edad,grado)
print(f"Datos del estudiante registrado:\nNombre: {Estudiante1.nombre}\nEdad: {Estudiante1.edad}\nGrado: {Estudiante1.grado}")

