# 03 Se ingresan 50 números enteros. Determinar Pares y Impares


cantidad_numeros = int(input("Cantidad de numeros:"))

for cantidad in range(1, cantidad_numeros+1):
    resultado = (cantidad % 2) != 0
    if (resultado == 0):  # Par
        print(f"Numero {cantidad}: Par")

    else:  # impar
        print(f"Numero {cantidad}: Impar")
