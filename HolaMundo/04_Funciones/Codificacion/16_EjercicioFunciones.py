"""
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero se recomienda no usarla.
"""


def longitud_lista(lista):
    contador = 0
    # 1. for len_lista in lista:
    #    print(len_lista)
    while True:
        try:
            lista[contador]
            contador += 1
        except Exception:
            break
    return print(contador)


lista = [1, 2, 3, 4, "Franco", "Galan", 5, 6, 7, 8]
longitud_lista(lista)
