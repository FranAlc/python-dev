"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.
"""

# funciones
# 1.


def vocales(caracter):
    if len(caracter) == 1:
        if caracter == "a" or caracter == "A":
            print("La 'a' es vocal.")
        elif caracter == "e" or caracter == "E":
            print("La 'e' es vocal.")
        elif caracter == "i" or caracter == "I":
            print("La 'i' es vocal.")
        elif caracter == "o" or caracter == "O":
            print("La 'o' es vocal.")
        elif caracter == "u" or caracter == "U":
            print("La 'u' es vocal.")
        else:
            print(f"La '{caracter}' no es una vocal.")
    else:
        print("Caracter no valido.")

# 2.


def vocal(caracter):
    vocales = "aeiouAEIOU"
    if len(caracter) == 1:
        if caracter in vocales:
            print(f"La letra {caracter} es una vocal.")
        else:
            print(f"La letra {caracter} no es una vocal.")
    else:
        print("Caracter no valido.")


# main
char = input("Digite un caracter: ")

vocal(char)
