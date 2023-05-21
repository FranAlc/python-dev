# 08 Realizar un programa que ingrese dos números e indique si el primer número es divisible por el segundo.

num1 = int(input("Ingresar un numero: "))
num2 = int(input("Ingresar un segundo numero: "))

resultado = num1 % num2 == 0

if (resultado != 0):
    print(f"{num1} es divisible por el segundo")
else:
    print(f"{num1} no es divisible por el segundo")
