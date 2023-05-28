# 24 Construya un algoritmo que, dados tres números, muestre el mensaje “IGUALES” si la suma de los dos primeros es igual al otro número y el mensaje “DISTINTOS” en caso contrario.

# entrada de datos
num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))
num3 = float(input("Numero 3: "))

# proceso de datos
r = num1 + num2

if r == num3:
    # salida 1
    print("Iguales")

else:
    # salida 2
    print("Distintos")
