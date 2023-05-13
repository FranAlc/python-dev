"""
04 Ingresar 3 valores reales y:
a. Si los dos primeros son mayores al tercero informar “MAYORES AL TERCERO”.
b. Si los tres son iguales informar “TRES IGUALES .
c. Si alguno de los dos primeros es menor al tercero informar “ALGUNO ES MENOR”.
"""

num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa un segundo numero: "))
num3 = float(input("Ingresa un tercer numero: "))


if (num1 > num3) and (num2 > num3):
    print("Mayores al tercero")
elif (num1 == num2) and (num1 == num3) and (num2 == num3):
    print("Son iguales")
elif (num1 < num3) | (num2 < num3):
    print("Alguno es menor")
