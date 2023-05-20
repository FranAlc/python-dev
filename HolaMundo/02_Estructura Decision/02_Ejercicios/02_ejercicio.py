# 02 Dados tres números determinar e informar con un mensaje si el primer número ingresado es menor que los otros dos.

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un segundo numero: "))
num3 = int(input("Ingresa un tercer numero: "))

if (num1 < num2) and (num1 < num3):
    print(f"{num1} es menor a {num2} y {num3}")
elif (num2 < num1) and (num2 < num3):
    print(f"{num2} es menor a {num1} y {num3}")
elif (num3 < num1) and (num3 < num2):
    print(f"{num3} es menor a {num1} y {num2}")
