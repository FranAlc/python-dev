"""
Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado.
"""

# funcion


def superposicion(lista1, lista2):

    for elementos in lista1:
        for elementos2 in lista2:
            if elementos == elementos2:
                return True
            else:
                return False


# main
lista1 = [20, "Franco", "Galan"]
lista2 = [20, "Daniel", "Martinez"]

consola = superposicion(lista1, lista2)

print(consola)
