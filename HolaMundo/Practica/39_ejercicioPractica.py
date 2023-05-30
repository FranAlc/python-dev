"""
a >> La funcion principal (Decorador)
b >> Funcion de decorar
c >> La funcion decorada
"""
"""
# 1


def funcion_a(funcion_b):

   def funcion_c():
        print("Hola, funcion c")
        funcion_b()  # >> llamamos a funcion b
    return funcion_c


@funcion_a
def saludar():
    print("Hola, estoy aprendiendo python")


saludar()  # no solo retornara la funcion_c , tambien devuelve funcion_b
"""
# 2
# funcion


def funcion_a(funcion_b):

    def funcion_c():
        # funcion anidada
        print(">>>Antes del llamado.")
        funcion_b()  # >> llamamos a funcion b
        print(">>>Despues del llamado.")  # extendiendo funcionalidades
    return funcion_c

# funcion decorada


@funcion_a  # >> podemos ejecutar codigo antes o despues de su llamado
def saludar():
    print("Hola, estoy aprendiendo python")


saludar()  # no solo retornara la funcion_c , tambien devuelve funcion_b

# 1.Los decoradores reciben como argumento otra funcion y a su vez retorna una nueva funcion
# 2. Esta nueva funcion no seria mas que la funcion decorada
# 3. Extienden funcionalidades sin tener que modificar la funcion original
