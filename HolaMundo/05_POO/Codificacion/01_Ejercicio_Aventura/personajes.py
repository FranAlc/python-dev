# Clase personaje
import random
from enemigos import *


class Guerrero:

    # Atributos de la clase Guerrero

    def __init__(self):
        self.nombre = ""
        self.estatura = None
        self.tipo_arma = ""
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
        acumulador = 0
        opc = 1
        aciertos = []
        fallos = []
        golpes = ["Golpeaste al Monstruo!".title(), "Fallaste".title()]
        start = random.choice(golpes)
        print(f"{self.nombre.title()}, debes atacar..\n")

        while acumulador != 2000 and self.vida > 0:
            if start == golpes[0]:
                print("Lograste golpearlo !!".title())
                acumulador += self.fuerza
                aciertos.append(acumulador)
                if sum(aciertos) == 2000:
                    for i in aciertos:
                        print(i)
                    print("Derrotaste al monstruo".upper())

            elif start == golpes[1]:
                print("Fallaste !!".title())
                acumulador += self.fallaste
                fallos.append(acumulador)
