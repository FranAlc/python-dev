# Clase enemigo
import personajes
from personajes import *


class Monstruos:
    def __init__(self):
        self.nombre = "Eva"
        self.vida = 800
        self.defensa = 0
        self.color = "Verde"
    # metodo

    def atributos(self):
        print("---------------------------------------")
        print(f"NOMBRE ENEMIGO: {self.nombre.upper()}.")
        print(f"VIDA: {self.vida}.")
        print(f"El color del enemigo es {self.color}.")
        print("---------------------------------------")
