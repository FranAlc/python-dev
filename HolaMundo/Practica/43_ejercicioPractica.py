temperatura = 12.0
nombre = "Franco"


def mi_funcion(nombre):

    global temperatura  # haciendo uso de global
    temperatura = 9.0

    print(f"Hola {nombre} hoy hace {temperatura} grados")


mi_funcion(nombre)

print(temperatura)
