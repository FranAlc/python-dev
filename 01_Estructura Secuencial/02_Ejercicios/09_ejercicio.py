# 09 Confeccionar un programa que solicite el ingreso del valor del radio (r) de un círculo y con dicho valor calcule la superficie del círculo, la longitud de la circunferencia (perímetro) y el volumen de la esfera.

import math

radio = float(input("Ingresa el valor del radio: "))

superficie = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
volumen = (4/3) * math.pi * radio ** 3

print(
    f"La superficie: {radio}\nEl perimetro: {perimetro}\nEl volumen: {volumen}\n")
