# Clase personaje
import enemigos
from enemigos import *


class Guerrero:
    cant_golpes = 0
    # Atributos de la clase Guerrero

    def __init__(self):
        self.nombre = ""
        self.estatura = None
        self.tipo_arma = ""
        self.fuerza = None
        self.vida = 1000

    # Metodos
    def atributos(self):
        print("\nAtributos del guerrero: ")
        print(f"Nombre del Guerrero: {self.nombre.title()}.")
        print(f"Estatura: {self.estatura}.")
        print(f"Tipo de arma: {self.tipo_arma.title()}.")
        print(f"FUERZA: {self.fuerza}.")  # daño
        print(f"VIDA: {self.vida}.")

    def atacar(self):
        print(f"{self.nombre}, debes atacar")
