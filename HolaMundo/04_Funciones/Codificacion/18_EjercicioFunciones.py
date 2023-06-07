"""
Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.
"""

# funciones

# suma


def sumar(lista_num):

    return print(f"La suma de los numeros es: {sum(lista_num)}")

# multiplicar


def multip(lista_num):
    # multiplico el producto que vale 1 por cada elemento de la lista
    producto = 1
    for elemento in lista_num:
        producto *= elemento
    return print(f"La multiplicacion de los numeros es: {producto}")


# main
suma = [1, 2, 3, 4]
multiplicacion = [1, 2, 3, 4]


# suma
print(suma)
sumar(suma)
# multiplicacion
print(multiplicacion)
multip(multiplicacion)
