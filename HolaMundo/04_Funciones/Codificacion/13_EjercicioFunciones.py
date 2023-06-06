"""
Digitar una funcion llamada max_in_list() que devuelva el numero mayor dentro de una lista nombrada en el "main".
"""


def max_in_list(lista):
    numero_mayor = max(lista)
    return numero_mayor


lista_de_numeros = [1, 2, 3, 4, 5, 6, 8, 58, 96, 78, 51]

numero_max = max_in_list(lista_de_numeros)
print(f"Numero mayor: {numero_max}")
