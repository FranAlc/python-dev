# Clase enemigo

from personajes import *


class Monstruos:
    def __init__(self):
        self.nombre = "Eva"
        self.vida = 2000
        self.defensa = 0
        self.color = "Verde"
    # metodo

    def atributos(self):
        print("---------------------------------------")
        print(f"NOMBRE ENEMIGO: {self.nombre.upper()}.")
        print(f"VIDA: {self.vida}.")
        print(f"El color del enemigo es {self.color}.")
        print("---------------------------------------")

    def atacar(self):
        acumulador = 0
        aciertos = []
        fallos = []
        golpes = []
        golpes.append("Golpeaste al Guerrero!")
        golpes.append("Fallaste!")
        start = random.choice(golpes)
        if start == [0]:
            acumulador += self.fuerza
            aciertos.append(acumulador)
            if sum(aciertos) == 2000:
                print("Derrotaste al Guerrero!".title())

        elif start == [1]:
            acumulador += self.fallaste
            fallos.append(acumulador)

        print(f"{self.nombre.title()}, debes atacar..")
