"""
a >> La funcion principal (Decorador)
b >> Funcion de decorar
c >> La funcion decorada
"""


def funcion_a(funcion_b):

    def funcion_c():
        print("Hola, funcion c")
        funcion_b()  # >> llamamos a funcion b
    return funcion_c


@funcion_a
def saludar():
    print("Hola, estoy aprendiendo python")


saludar()  # no solo retornara la funcion_c , tambien devuelve funcion_b
