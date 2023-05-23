# 14 Determine la distancia entre dos puntos en el espacio.
# (x1,y1, z1) y (x2, y2, z2)

punto_a = []
punto_b = []

for i in range(0, 6):
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
