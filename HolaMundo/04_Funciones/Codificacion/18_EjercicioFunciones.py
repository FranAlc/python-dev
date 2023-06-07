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

# dividir


def dividir(lista_num):
    acumulador = 0
    contador = 0
    for elementos in lista_num:
        acumulador += elementos
        contador += 1
        resultado = acumulador / contador
    print(f"La division de los numeros es: {resultado}")


# main
suma = [1, 2, 3, 4]
multiplicacion = [1, 2, 3, 4]
division = [1, 2, 3, 4]

# suma
print(suma)
sumar(suma)
# multiplicacion
print(multiplicacion)
multip(multiplicacion)
# division
print(division)
dividir(division)
