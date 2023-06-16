import random
from personajes import *
from enemigos import *

enemigo = Monstruos()
personaje = Guerrero()


class Pelea_Guerrero_Monstruo:

    def __init__(self):
        self.golpes_enemigo = []
        self.golpes_guerrero = []
        self.golpes = ["ACERTO EL GOLPE !!", "FALLO EL GOLPE !!"]
        self.pelea = ["Guerrero", "Monstruo"]
        self.start = None
        self.resultado = None
        self.cant_golpes_guerrero = []
        self.cant_golpes_enemigo = []
        self.dato_final = "lograste vencer al monstruo !!"
        self.dato_final2 = "fuiste derrotado!!"
        self.combate2()

    def combate(self):
        start = random.choice(self.pelea)
        print(f"Comienza atacando {start}")
        # comienza pelea guerrero
        if start == self.pelea[0]:
            for i in range(1, 9):
                personaje.atacar()  # ataca el personaje
                self.resultado = random.choice(self.golpes)
                print(f"{self.resultado}\n")
                self.golpes_guerrero.append(self.resultado)

                enemigo.atacar()  # ataca el enemigo
                self.resultado = random.choice(self.golpes)
                print(f"{self.resultado}\n")
                self.golpes_enemigo.append(self.resultado)
            self.cant_golpes_guerrero = self.golpes_guerrero.count(
                "ACERTO EL GOLPE !!")
            self.cant_golpes_enemigo = self.golpes_enemigo.count(
                "ACERTO EL GOLPE !!")
            if self.cant_golpes_guerrero > self.cant_golpes_enemigo:
                print(
                    f"CANTIDAD DE GOLPES QUE LE DISTE = {self.cant_golpes_guerrero}")
                print(f"{self.dato_final.upper()}")
                self.combate2()
            else:
                print(
                    f"CANTIDAD DE GOLPES DADOS POR EL MONSTRUO = {self.cant_golpes_enemigo}")
                print(f"{personaje.nombre} {self.dato_final2.upper()}")

        # comienza pelea monstruo
        else:
            for i in range(1, 9):
                enemigo.atacar()  # ataca el enemigo
                self.resultado = random.choice(self.golpes)
                print(f"{self.resultado}\n")
                self.golpes_enemigo.append(self.resultado)

                personaje.atacar()  # ataca el personaje
                self.resultado = random.choice(self.golpes)
                print(f"{self.resultado}\n")
                self.golpes_guerrero.append(self.resultado)

            self.cant_golpes_guerrero = self.golpes_guerrero.count(
                "ACERTO EL GOLPE !!")
            self.cant_golpes_enemigo = self.golpes_enemigo.count(
                "ACERTO EL GOLPE !!")
            if self.cant_golpes_guerrero > self.cant_golpes_enemigo:
                print(
                    f"CANTIDAD DE GOLPES QUE LE DISTE = {self.cant_golpes_guerrero}")
                print(f"{self.dato_final.upper()}")

            else:
                print(
                    f"CANTIDAD DE GOLPES DADOS POR EL MONSTRUO = {self.cant_golpes_enemigo}")
                print(f"{personaje.nombre} {self.dato_final2.upper()}")

    def combate2(self):
        print(f"\nMaravilloso {personaje.nombre} has logrado GANAR !")


class Pelea_Guerrero_Dragon:
    def __init__(self):
        self.pelear = None
