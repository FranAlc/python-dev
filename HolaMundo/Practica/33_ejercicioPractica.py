# Creacion de diccionarios dentro de una funcion
def usuarios(**kwargs):
    print(kwargs)


users = usuarios(martin=[10, 50, 30], nombre="Franco")
print(users)

# (*args) TUPLA
# (**kwargs) DICCIONARIO


def combinacion(*args, **kwargs):
    print("Tupla: ", args)
    print("Dict:", kwargs)


combinacion(1, 2, 3, 4, 5, nombre="Franco", apellido="Galan", Skill="Python")
