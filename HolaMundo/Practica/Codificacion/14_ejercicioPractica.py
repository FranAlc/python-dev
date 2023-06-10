# 14 Determine la distancia entre dos puntos en el espacio.
# (x1,y1, z1) y (x2, y2, z2)

import math
punto_a = []
punto_b = []

for i in range(1):
    x1 = float(input("Digite el valor de x1: "))
    y1 = float(input("Digite el valor de y1: "))
    z1 = float(input("Digite el valor de z1: "))
    x2 = float(input("\nDigite el valor de x2: "))
    y2 = float(input("Digite el valor de y2: "))
    z2 = float(input("Digite el valor de z2: "))
    # a
    punto_a.append(round(x1))
    punto_a.append(round(y1))
    punto_a.append(round(z1))
    # b
    punto_b.append(round(x2))
    punto_b.append(round(y2))
    punto_b.append(round(z2))
    print(f"Primer punto {punto_a}")
    print(f"Segundo punto {punto_b}")

    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print("--------------------------------------------------")
    print("Ejercicio 14: Ejercicio - Distancia de dos puntos")
    print("--------------------------------------------------")
    print("Datos ingresados:")
    print(f"Lista primer punto: {punto_a}")
    print(f"Lista segundo punto: {punto_b}")
    print("\nSalida:")
    print("--------------------------------------------------")
    print(f"La distancia es: {d}")
    print("--------------------------------------------------")
