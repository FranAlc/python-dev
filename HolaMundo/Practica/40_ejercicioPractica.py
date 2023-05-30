# Numeros pares >> GENERADORES

def pares():  # convierte a Generador >> Lazy iterator
    for num in range(0, 100, 2):
        yield num  # a diferencia de return, el yield sirve para generadores, suspenderemos de forma momentanea la funcion
        # ademas deja seguir escribiendo codigo luego de nombrar a yield
        print("Numero par:")


print(pares())  # ahora devuelve un objeto

for par in pares():  # llamo a la funcion pares()
    print(par)
