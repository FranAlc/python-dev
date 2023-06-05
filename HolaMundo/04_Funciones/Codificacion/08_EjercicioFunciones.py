"""
Crea una función "calcular_max_min" que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
Crea un programa que pida números por teclado y muestre el máximo y el mínimo.
"""


# Funcion
def calcular_max_min(lista_valores):
    print("Valor maximo:", max(lista_valores))
    print("Valor minimo", min(lista_valores))


def calcular_max_min_xteclado(num1, num2):
    if num1 > num2:
        return print(f"{num1} es mayor")
    else:
        return print(f"{num2} es mayor")


# main
print("Valor maximo y minimo dentro de una lista:")
lista_valores = [2, 5, 6, 8, 20, 5, 18, 901, 5, 8, 748, 15, 7]
print(lista_valores)
calcular_max_min(lista_valores)

print("\nValor maximo y minimo ingresado por teclado:")
num1 = int(input("Digite un numero:"))
num2 = int(input("Digite un numero:"))
calcular_max_min_xteclado(num1, num2)
