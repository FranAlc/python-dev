# 28 Leer tres números enteros y, si el primero de ellos es negativo, calcular el producto de los tres, en caso contrario calcular la suma de ellos.

num1 = int(input("Num: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

if num1 < 0 or num2 < 0 or num3 < 0:
    producto = num1 * num2 * num3
    print(f"Producto: {producto}")
else:
    suma = num1 + num2 + num3
    print(f"Suma: {suma}")
