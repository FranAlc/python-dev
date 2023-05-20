# 03 Confeccionar un programa que pueda ingresar 2 números enteros y calcule e informe con mensajes aclaratorios la suma, el producto, el cociente y el resto.

numero_entero1 = int(input("Ingresa un numero entero: "))
numero_entero2 = int(input("Ingresa un segundo numero entero: "))

suma = numero_entero1 + numero_entero2
producto = numero_entero1 * numero_entero2
cociente = numero_entero1 // numero_entero2
modulo = numero_entero1 % numero_entero2

print(
    f"Suma: {suma}\nProducto: {producto}\nCociente: {cociente}\nModulo: {modulo}\n")
