import random
from personajes import *
from enemigos import *

enemigo = Monstruos()
personaje = Guerrero()


class Pelea_Guerrero_Monstruo:
    def __init__(self):
        self.lista_golpes = []
        self.golpes = ["ACERTO EL GOLPE !!", "FALLO EL GOLPE !!"]
        self.pelea = ["Monstruo", "Guerrero"]
        self.start = None

    def combate(self):
        start = random.choice(self.pelea)
        print(f"Comienza atacando {start}")
        
