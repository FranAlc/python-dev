import random
from personajes import *
from enemigos import *

enemigo = Monstruos()
personaje = Guerrero()
enemigo_dragon = Dragon()


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
        self.fin_del_combate_win()
        self.fin_del_combate_lose()

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
                print(
                    f"CANTIDAD DE GOLPES DADOS POR EL MONSTRUO = {self.cant_golpes_enemigo}")
                print(f"{self.dato_final.upper()}")
                self.fin_del_combate_win()
            else:
                print(
                    f"CANTIDAD DE GOLPES DADOS POR EL MONSTRUO = {self.cant_golpes_enemigo}")
                print(
                    f"CANTIDAD DE GOLPES QUE LE DISTE = {self.cant_golpes_guerrero}")
                print(f"{personaje.nombre} {self.dato_final2.upper()}")
                self.fin_del_combate_lose()

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
                print(
                    f"CANTIDAD DE GOLPES DADOS POR EL MONSTRUO = {self.cant_golpes_enemigo}")
                print(f"{self.dato_final.upper()}")
                self.fin_del_combate_win()

            else:
                print(
                    f"CANTIDAD DE GOLPES DADOS POR EL MONSTRUO = {self.cant_golpes_enemigo}")
                print(
                    f"CANTIDAD DE GOLPES QUE LE DISTE = {self.cant_golpes_guerrero}")
                print(f"{personaje.nombre} {self.dato_final2.upper()}")
                self.fin_del_combate_lose()

    def fin_del_combate_win(self):
        print(f"\nMaravilloso {personaje.nombre} has logrado GANAR !")

    def fin_del_combate_lose(self):
        print(f"\nHas sido derrotado {personaje.nombre} pero no te desanimes!")

# 2 pelea con otro enemigo


class Pelea_Guerrero_Dragon:
    def __init__(self):
        self.golpes = ["Lograste DAÑARLO !!", "Has FALLADO"]
        self.random_personajes = None
        self.comienza_atacando = ["Guerrero", "Dragon"]
        self.random_golpes = None
        self.vida_personaje = []
        self.vida_enemigo = []
        self.resul = None
        personaje.vida = 2000

    def pelea(self):

        self.random_personajes = random.choice(self.comienza_atacando)
        if self.random_personajes == self.comienza_atacando[0]:
            # Comienza atacando el personaje
            print("Comienzas atacando")

            self.random_golpes = random.choice(self.golpes)
            if self.random_golpes == self.golpes[0]:
                for i in range(1, 9):
                    # comienza personaje
                    print("Guerrero: ", self.golpes[0])
                    enemigo_dragon.vida -= 400
                    self.vida_enemigo.append(enemigo_dragon.vida)
                    print("\nVida enemigo: ", self.vida_enemigo)

                    if self.random_golpes == self.golpes[1]:
                        print("Guerrero ", self.golpes[1])

                    # sigue dragon

                    print("Dragon ", self.golpes[0])
                    personaje.vida -= 200
                    self.vida_personaje.append(personaje.vida)
                    print("\nVida personaje: ", self.vida_personaje)

                    if self.random_golpes == self.golpes[1]:
                        print("Dragon ", self.golpes[1])

                if sum(self.vida_enemigo) < 0:
                    print(self.vida_enemigo)
                    print("GANASTE , Mataste al dragon")

                elif sum(self.vida_personaje) < 0:
                    print(self.vida_personaje)
                    print("PERDISTE, el Dragon acabo contigo")
            else:
                for i in range(1, 9):
                    # comienza personaje
                    print("Guerrero: ", self.golpes[0])
                    enemigo_dragon.vida -= 400
                    self.vida_enemigo.append(enemigo_dragon.vida)
                    print("\nVida enemigo: ", self.vida_enemigo)

                    if self.random_golpes == self.golpes[1]:
                        print("Guerrero ", self.golpes[1])

                    # sigue dragon

                    print("Dragon ", self.golpes[0])
                    personaje.vida -= 200
                    self.vida_personaje.append(personaje.vida)
                    print("\nVida personaje: ", self.vida_personaje)

                    if self.random_golpes == self.golpes[1]:
                        print("Dragon ", self.golpes[1])

                if sum(self.vida_enemigo) < 0:
                    print(self.vida_enemigo)
                    print("\nGANASTE , Mataste al dragon")

                elif sum(self.vida_personaje) < 0:
                    print(self.vida_personaje)
                    print("\nPERDISTE, el Dragon acabo contigo")

    # pelea dragon
        elif self.random_personajes == self.comienza_atacando[1]:

            print("Comienza atacando el enemigo")

            self.random_golpes = random.choice(self.golpes)
            if self.random_golpes == self.golpes[0] or self.random_golpes == self.golpes[1]:
                for i in range(1, 9):
                    # comienza dragon
                    print("Dragon ", self.golpes[0])
                    personaje.vida -= 200
                    self.vida_enemigo.append(personaje.vida)
                    print("Vida personaje: ", self.vida_personaje)
                    if self.random_golpes == self.golpes[1]:
                        print("Dragon ", self.golpes[1])

                    # sigue personaje
                    print("Guerrero: ", self.golpes[0])
                    enemigo_dragon.vida -= 400
                    self.vida_enemigo.append(enemigo_dragon.vida)
                    print("Vida enemigo: ", self.vida_enemigo)
                    if self.random_golpes == self.golpes[1]:
                        print("Guerrero ", self.golpes[1])

                if sum(self.vida_enemigo) < 0:
                    print(self.vida_enemigo)
                    print("GANASTE , Mataste al dragon")

                elif sum(self.vida_personaje) < 0:
                    print(self.vida_personaje)
                    print("PERDISTE, el Dragon acabo contigo")

        """

            # Comienza atacando el enemigo "Dragon"
            print("Comienza atacando el enemigo Dragon")
            while enemigo.vida == 0 and personaje.vida == 0:

                self.random_golpes = random.choice(self.golpes)
                if self.random_golpes == self.golpes[0]:
                    print("Dragon, ", self.golpes[0])
                    self.resul = personaje.vida - 200
                    self.vida_enemigo.append(self.resul)

                personaje.atacar()
                self.random_golpes = random.choice(self.golpes)
                if self.random_golpes == self.golpes[0]:
                    print("Guerrero, ", self.golpes[0])
                    self.resul = enemigo.vida - 400
                    self.vida_enemigo.append(self.resul)
           
        """
