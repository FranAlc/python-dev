"""
Definir una función num_max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una función max() incorporada, pero realizarla sin la funcion max() es un
muy buen ejercicio.)
"""


def num_max(num1, num2):
    if num1 > num2:
        return print(f"El numero {num1} es mayor.")
    else:
        return print(f"El numero {num2} es mayor.")


numero1 = int(input("Digite un numero: "))
numero2 = int(input("Digite un numero: "))

num_max(numero1, numero2)
