# 06 Confeccionar un programa que permita ingresar 4 números enteros, de a uno por vez y determine el menor  valor y su número de orden. Informe los valores ingresados e identifique al menor con mensaje aclaratorio.
"""
num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa un segundo numero entero: "))
num3 = int(input("Ingresa un tercer numero entero: "))
num4 = int(input("Ingresa un cuarto numero entero: "))

# menor valor
# num1
if (num1 < num2) and (num1 < num3) and (num1 < num4):
    print(f"El numero {num1} es menor a {num2},{num3} y {num4}.")
# num2
elif (num2 < num1) and (num2 < num3) and (num2 > num4):
    print(f"El numero {num2} es menor a {num1},{num3} y {num4}.")
# num3
elif (num3 < num1) and (num3 < num2) and (num3 > num4):
    print(f"El numero {num3} es menor a {num1},{num2} y {num4}.")
# num4
elif (num4 < num1) and (num4 < num3) and (num4 < num2):
    print(f"El numero {num4} es menor a {num1},{num2} y {num3}.")

# numero de orden
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

# Identificar el número más pequeño de la lista
if num1 <= num2 and num1 <= num3 and num1 <= num4:
    menor = num1
    print(f"El número {menor} es el más pequeño.")
elif num2 <= num1 and num2 <= num3 and num2 <= num4:
    menor = num2
    print(f"El número {menor} es el más pequeño.")
elif num3 <= num1 and num3 <= num2 and num3 <= num4:
    menor = num3
    print(f"El número {menor} es el más pequeño.")
else:
    menor = num4
    print(f"El número {menor} es el más pequeño.")

# Ordenar los números de menor a mayor utilizando declaraciones condicionales if
if num1 <= num2 and num1 <= num3 and num1 <= num4:
    menor = num1
    if num2 <= num3 and num2 <= num4:
        medio1 = num2
        if num3 <= num4:
            medio2 = num3
            mayor = num4
        else:
            medio2 = num4
            mayor = num3
    elif num3 <= num2 and num3 <= num4:
        medio1 = num3
        if num2 <= num4:
            medio2 = num2
            mayor = num4
        else:
            medio2 = num4
            mayor = num2
    else:
        medio1 = num4
        if num2 <= num3:
            medio2 = num2
            mayor = num3
        else:
            medio2 = num3
            mayor = num2
elif num2 <= num1 and num2 <= num3 and num2 <= num4:
    menor = num2
    if num1 <= num3 and num1 <= num4:
        medio1 = num1
        if num3 <= num4:
            medio2 = num3
            mayor = num4
        else:
            medio2 = num4
            mayor = num3
    elif num3 <= num1 and num3 <= num4:
        medio1 = num3
        if num1 <= num4:
            medio2 = num1
            mayor = num4
        else:
            medio2 = num4
            mayor = num1
    else:
        medio1 = num4
        if num1 <= num3:
            medio2 = num1
            mayor = num3
        else:
            medio2 = num3
            mayor = num1
elif num3 <= num1 and num3 <= num2 and num3 <= num4:
    menor = num3
    if num1 <= num2 and num1 <= num4:
        medio1 = num1
        if num2 <= num4:
            medio2 = num2
            mayor = num4
        else:
            medio2 = num4
            mayor = num2
    elif num2 <= num1 and num2 <= num4:
        medio1 = num2
        if num1 <= num4:
            medio2 = num1
