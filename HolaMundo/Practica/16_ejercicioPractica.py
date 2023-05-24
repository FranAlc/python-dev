# 16 Imprimir el menor de dos numeros

# entrada de datos
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

# proceso de datos
if num1 > num2:
    # salida 1
    print(f"{num2} es menor a {num1}")
elif num2 > num1:
    # salida 2
    print(f"{num1} es menor a {num2}")
else:
    print(f"Los numeros {num1} y {num2} son iguales")
