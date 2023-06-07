"""
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. 
"""


def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return print(f"El numero mayor es {n1}.")
    elif n2 > n1 and n2 > n3:
        return print(f"El numero mayor es {n2}.")
    elif n3 > n1 and n3 > n2:
        return print(f"El numero mayor es {n3}.")
    else:
        return print("Los numeros son iguales")


numero1 = int(input("Digite un numero: "))
numero2 = int(input("Digite un segundo numero: "))
numero3 = int(input("Digite un tercer numero: "))

max_de_tres(numero1, numero2, numero3)
