# Clase personaje
import random
from enemigos import *


class Guerrero:

    # Atributos de la clase Guerrero

    def __init__(self):
        self.nombre = "Guerrero"
        self.estatura = None
        self.tipo_arma = "tu arma."
        self.fuerza = None
        self.defensa = 200
        self.vida = 2000
        self.fallaste = 0

    # Metodos
    def atributos(self):
        print("\nAtributos del guerrero: ")
        print(f"Nombre del Guerrero: {self.nombre.title()}.")
        print(f"Estatura: {self.estatura}.")
        print(f"Tipo de arma: {self.tipo_arma.title()}.")
        print(f"FUERZA: {self.fuerza}.")  # daño
        print(f"VIDA: {self.vida}.")
        print(f"DEFENSA: {self.defensa}.")

    def atacar(self):
        print(f"Te toca atacar con {self.tipo_arma}..".upper())
