"""
Digitar una funcion llamada min_in_list() que devuelva el numero menor dentro de una lista nombrada en el "main".
"""

# funcion


def min_in_list(lista):
    numero_menor = min(lista)
    return numero_menor


# main
lista_de_numeros = [1, 2, 3, 4, 5, 6, 8, 58, 96, 78, 51]

numero_max = min_in_list(lista_de_numeros)
print(f"Numero menor: {numero_max}")
