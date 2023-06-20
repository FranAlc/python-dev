# Clase enemigo
import random
from personajes import *


class Monstruos:
    def __init__(self):
        self.nombre = "Eva"
        self.vida = 3200
        self.defensa = 0
        self.color = "Verde"
        self.tipo_arma = "Baston"
        self.resultado = None
    # metodo

    def atributos(self):
        print("---------------------------------------")
        print(f"NOMBRE ENEMIGO: {self.nombre.upper()}.")
        print(f"VIDA: {self.vida}.")
        print(f"Defensa: {self.defensa}.")
        print(f"El color del enemigo es {self.color}.")
        print("---------------------------------------")

    def atacar(self):
        str_sorteo = (f"ATACA CON EL {self.tipo_arma}",
                      "CONTINUA ATACANDO CON LAS GARRAS")
        self.resultado = random.choice(str_sorteo)
        if self.resultado == str_sorteo[0]:
            print(f"{self.nombre.title()} {str_sorteo[0]}..")
        else:
            print(f"{self.nombre.title()} {str_sorteo[1]}..")

class Dragon():
    def __init__(self):
        self.nombre = "Dragon"
        self.vida = 3000
        self.defensa = 0
        self.fuerza = 200
        self.color = "Rojo"
        self.tipo_arma = "Fuego"
        self.resultado = None
    # metodo

    def atributos(self):
        print("---------------------------------------")
        print(f"NOMBRE ENEMIGO: {self.nombre.upper()}.")
        print(f"VIDA: {self.vida}.")
        print(f"Defensa: {self.defensa}.")
        print(f"El color del enemigo es {self.color}.")
        print("---------------------------------------")

    