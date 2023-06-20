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
        self.vida_guerrero = 2000
        self.gana_personaje = None
        self.gana_Dragon = None

    def pelea(self):
        enemigo_dragon.atributos()
        self.random_personajes = random.choice(self.comienza_atacando)
        if self.random_personajes == self.comienza_atacando[0]:
            # Comienza atacando el personaje
            print("\nComienzas atacando")
            self.random_golpes = random.choice(self.golpes)
            if self.random_golpes == self.golpes[0] or self.random_golpes == self.golpes[1]:
                for i in range(100):
                    # comienza personaje
                    print("Guerrero: ", self.golpes[0])
                    enemigo_dragon.vida -= 400
                    self.vida_enemigo.append(enemigo_dragon.vida)
                    print("Vida enemigo: ", self.vida_enemigo, "\n")
                    if self.vida_enemigo[-1] < 0:
                        print("++++++++++++++++++++++++++++++++++++++++")
                        print("++   LOGRASTE VENCER AL DRAGON !!!    ++")
                        print(
                            f"++   VIDA FINAL DE TU PERSONAJE: {self.vida_guerrero}  ++")
                        print(
                            f"++   VIDA FINAL DEL DRAGON: {enemigo_dragon.vida}      ++")
                        print("++++++++++++++++++++++++++++++++++++++++")
                        enemigo_dragon.vida = 3000
                        self.vida_guerrero = 2000
                        break

                    # sigue dragon
                    print("Dragon ", self.golpes[0])
                    self.vida_guerrero -= 200
                    self.vida_personaje.append(self.vida_guerrero)
                    print("Vida personaje: ", self.vida_personaje, "\n")
                    if self.vida_personaje[-1] < 0:
                        print("\nEL DRAGON TE HA VENCIDO !!!")
                        enemigo_dragon.vida = 3000
                        self.vida_guerrero = 2000
                        break

    # pelea dragon
        elif self.random_personajes == self.comienza_atacando[1]:
            print("Comienza atacando el enemigo")
            self.random_golpes = random.choice(self.golpes)
            if self.random_golpes == self.golpes[0] or self.random_golpes == self.golpes[1]:
                for i in range(100):
                    # comienza dragon
                    print("Dragon ", self.golpes[0])
                    self.vida_guerrero -= 200
                    self.vida_personaje.append(self.vida_guerrero)
                    print("Vida personaje: ", self.vida_personaje, "\n")
                    if self.vida_personaje[-1] < 0:
                        print("\nEL DRAGON TE HA VENCIDO !!!")
                        enemigo_dragon.vida = 3000
                        self.vida_guerrero = 2000
                        break

                    # sigue personaje
                    print("Guerrero: ", self.golpes[0])
                    enemigo_dragon.vida -= 400
                    self.vida_enemigo.append(enemigo_dragon.vida)
                    print("Vida enemigo: ", self.vida_enemigo, "\n")
                    if self.vida_enemigo[-1] < 0:
                        print("++++++++++++++++++++++++++++++++++++++++")
                        print("++   LOGRASTE VENCER AL DRAGON !!!    ++")
                        print(
                            f"++   VIDA FINAL DE TU PERSONAJE: {self.vida_guerrero}  ++")
                        print(
                            f"++   VIDA FINAL DEL DRAGON: {enemigo_dragon.vida}      ++")
                        print("++++++++++++++++++++++++++++++++++++++++")
                        enemigo_dragon.vida = 3000
                        self.vida_guerrero = 2000
                        break

