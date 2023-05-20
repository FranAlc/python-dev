# 03 Confeccionar un programa que pueda determinar de 3 números enteros que se ingresan si alguno de ellos es igual a la suma de los otros dos.

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un segundo numero: "))
num3 = int(input("Ingresa un tercer numero: "))

# numero entero 1
if (num1 == (num2+num3)):
    print(f"{num1} es igual a la suma de {num2} + {num3}")
elif (num1 != (num2+num3)):
    print(f"{num1} es diferente a la suma de {num2} + {num3}")
# numero entero 2
elif (num2 == (num1+num3)):
    print(f"{num2} es igual a la suma de {num1} + {num3}")
elif (num2 != (num1+num3)):
    print(f"{num2} es diferente a la suma de {num1} + {num3}")
# numero entero 3
elif (num3 == (num1+num2)):
    print(f"{num3} es igual a la suma de {num1} + {num2}")
elif (num3 != (num1+num2)):
    print(f"{num3} es diferente a la suma de {num1} + {num2}")
