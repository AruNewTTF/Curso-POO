#Crear una clase PJ basica el cual tenga habilidades las cuales usar
import random as r

class personaje():
    def __init__(self,nombre,clase,vida):
        self.nombre = nombre
        self.clase = clase
        self.vida = vida
    def ataque(self):
        chance_de_fallo = r.randint(1,6)
        if chance_de_fallo == 1:
            print("Fallaste el ataque")
            return 0
        else:
            print("Has atinado!")
            return 25
    def defensa(self):
        print("Te proteges durante este turno")
        
p1 = personaje("Pipe","Guerrero",150)
Slime = personaje("Blob","Slime",75)
Enano = personaje("Juanin","Enano",50)

print(f"--------------------\nUn Slime ha aparecido")
while p1.vida > 0:
    if Slime.vida < 0 or Slime.vida == 0:
                print("Has ganado!")
                break
    print(f"--------------------\nTu Vida: {p1.vida}\nVida Enemigo {Slime.vida}")
    print("--------------------\n1. Atacar\n2. Defenderse\n3. Huir\n--------------------")
    accion = int(input("Es tu turno: "))
    
    if accion == 1:
        Slime.vida = Slime.vida - p1.ataque()
    elif accion == 2:
        p1.defensa()
    elif accion == 3:
        val = r.randint(1,2)
        if val == 1:
            print("Yo de aquí me largo..")
            break
        else:
            print("Nop, mejor sigo aquí")
    
    else:
        print("Escoge con sabiduría")