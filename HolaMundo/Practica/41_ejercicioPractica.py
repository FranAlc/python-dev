# Docstring
# Testear funciones
"""
Para testear se necesitan 3 comillas dobles.
Se llama a la funcion y se muestra aquello que realiza ejemplo :
#Usamos -m doctest
"""


def suma(num1, num2):
    """
    Funcion suma 2 numeros enteros.
    Argumentos:
    num1 (int)
    num2 (int)

    Se retorna la suma de los parametros mencionados:
    >>> suma(10,30)
    50
    >>> suma(50,50)
    100

    En caso que el resultado mencionado anteriormente no se cumpla saldra un error (linea 19)
    """
    return num1 + num2


print(suma.__doc__)  # muestra la documentacion dentro de la funcion
# Funcion help, puede realizar lo mismo
# print(help(suma))
