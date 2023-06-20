# Main
import random
from enemigos import *
from personajes import *
from pelea import *

# llamado de las clases localmente
personaje = Guerrero()
enemigo = Monstruos()


class Main:
    def bienvenida_al_personaje():
        print("\n-------------------------------------------------------------------------------------------")
        print(
            f"\tHOLA {personaje.nombre.upper()}, BIENVENIDO A ESTA AVENTURA.")
        print(
            f"PARA COMENZAR RECUERDE QUE SU VIDA ES DE {personaje.vida} y su fuerza es {personaje.fuerza} .")
        print(f"TENIENDO EN CUENTA ESO A LA HORA DE PELEAR SU FUERZA ES EL ATAQUE QUE INFLIGE AL ENEMIGO.")
        print(f"¡ BUENA SUERTE !")

    # funcion de datos del guerrero

    def personaje_guerrero():
        print("Digite los datos del guerrero:")
        nombre_personaje = input("Nombre: ")
        estatura_personaje = float(input("Estatura: "))
        print("Elija un arma y escribala tal cual aparece: ")
        print("1.Espada")
        print("2.Hacha")
        arma_personaje = input("Digite arma: ").title()
        # alojar datos anteriores
        personaje.nombre = nombre_personaje
        personaje.estatura = estatura_personaje
        if arma_personaje == "espada".title():
            personaje.tipo_arma = arma_personaje
            personaje.fuerza = 400
        elif arma_personaje == "hacha".title():
            personaje.tipo_arma = arma_personaje
            personaje.fuerza = 200
        personaje.atributos()

    # pelea

    def pelea():
        pelea = Pelea_Guerrero_Monstruo()
        pelea.combate()

    def pelea_dragon():
        pelea = Pelea_Guerrero_Dragon()
        pelea.pelea()

    print("\n\t--------¡ JUEGO DE AVENTURA !--------\n")
    print("Usted sera un personaje y debera luchar contra un enemigo...\n")
    personaje_guerrero()
    bienvenida_al_personaje()
    # resto del main

    print("Digite contra quien desea pelear: ")
    opcion_pelea = input("Dragon(Drg) // Monstruo(Monst): ")
    change_minus = opcion_pelea.lower()  # converti en minuscula la opcion
    while change_minus == "monst" or change_minus == "drg":

        if change_minus == "monst":
            print(f"\nGuerrero {personaje.nombre}")
            print("Seleccionaste pelear con un Monstruo.\n")
            # Enemigo informacion
            enemigo.atributos()
            # funcion pelea
            pelea()

        elif change_minus == "drg":
            pelea_dragon()

        # fin del bucle
        print("\nContinuar jugando: Escoge uno")
        opcion_pelea = input("Dragon(Drg) // Monstruo(Monst): ")
        change_minus = opcion_pelea.lower()

    print("\nENEMIGO NO ENCONTRADO..")


mostrar_main = Main()
