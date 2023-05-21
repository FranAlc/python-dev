# 01 Se ingresan 3 números distintos. Determinar el mayor

num1 = int(input("numero: "))
num2 = int(input("numero 2: "))
num3 = int(input("numero 3: "))

if (num1 > num2) and (num1 > num3):
    print(f"{num1} es mayor a {num2} y {num3}")
elif (num2 > num1) and (num2 > num3):
    print(f"{num2} es mayor a {num1} y {num3}")
elif (num3 > num2) and (num3 > num2):
    print(f"{num3} es mayor a {num1} y {num2}")
