# 06 Se ingresa un número entero de 3 cifras. Descomponerlo en unidad, decena y centena.

num = int(input("Ingresa un numero entero de 3 cifras: "))

unidad = num % 10
decena = (num // 10) % 10
centena = num // 100


print("El número ingresado descompuesto en unidades, decenas y centenas es:")
print(f"centena: {centena}\ndecena: {decena}\nunidad: {unidad}")
