"""
JUEGO DE NUMEROS.
"""

import random

# funciones


def condicional_numeros(numero):
    if num_random < numero:
        print("El numero random es menor.")
    elif num_random > numero:
        print("El numero random es mayor.")
    elif num_random == numero:
        print("ENCONTRASTE EL NUMERO!!")
        print("INGRESA EL CERO PARA FINALIZAR!\n")


def adivinar_numero():
    numero_random = random.randrange(1, 100)
    return numero_random


# main
num_random = adivinar_numero()
numero = int(input("Digite un numero: "))

while numero != 0:
    condicional_numeros(numero)
    numero = int(input("Digite un numero: "))
print("Fin del juego!")
