# Numeros pares >> GENERADORES
"""
def pares():  # convierte a Generador >> Lazy iterator
    for num in range(0, 100, 2):
        yield num  # a diferencia de return, el yield sirve para generadores, suspenderemos de forma momentanea la funcion
        # ademas deja seguir escribiendo codigo luego de nombrar a yield
        print("Numero par:")


print(pares())  # ahora devuelve un objeto

for par in pares():  # llamo a la funcion pares()
    print(par)

"""


def pares():  # Lazy iterator
    for num in range(0, 100, 2):
        yield num  # suspende ejecucion


generador = pares()

# Forma 1
# 1. Generar elementos conformes a demanda, siempre que los necesitemos
# 2. Ventaja de uso de memoria
print(next(generador))

print("ejecutamos codigo normalmente")

print(next(generador))

# Forma 2 dando uso de try y except
generador = pares()
while True:
    try:
        par = next(generador)
    except StopIteration:
        print("Finalizo el generador")
        break
