# 05 Se ingresan 3 números enteros. Informarlos en orden creciente

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un segundo numero: "))
num3 = int(input("Ingresa un tercer numero: "))

# numero 1
if (num1 > num2) and (num1 > num3) and (num2 > num3):
    print(f"Orden creciente: {num1}, {num2} , {num3}")
elif (num1 > num2) and (num1 > num3) and (num3 > num2):
    print(f"Orden creciente: {num1}, {num3} , {num2}")
elif (num1 == num2) and (num1 > num3):
    print(f"Orden creciente: {num1}, {num2} , {num3}")
elif (num1 == num3) and (num1 > num2):
    print(f"Orden creciente: {num1}, {num3} , {num2}")

# numero 2
elif (num2 > num1) and (num2 > num3) and (num1 > num3):
    print(f"Orden creciente: {num2}, {num1} , {num3}")
elif (num2 > num1) and (num2 > num3) and (num3 > num1):
    print(f"Orden creciente: {num2}, {num3} , {num1}")
elif (num2 == num1) and (num2 > num3):
    print(f"Orden creciente: {num2}, {num1} , {num3}")
elif (num2 == num3) and (num2 > num1):
    print(f"Orden creciente: {num2}, {num3} , {num1}")

# numero 3
elif (num3 > num1) and (num3 > num2) and (num2 > num1):
    print(f"Orden creciente: {num3}, {num2} , {num1}")
elif (num3 > num1) and (num3 > num2) and (num1 > num2):
    print(f"Orden creciente: {num3}, {num1} , {num2}")
