# 26 Algoritmo, que calcule el tiempo de encuentro de 2 vehículos que van en sentido opuesto, teniendo como datos la distancia inicial que los separa y la velocidad de cada uno.

# entrada de datos
distancia_inicial = float(input("Digite la distancia: "))
velocidad_v1 = float(input("Digite velocidad vehiculo 1: "))
velocidad_v2 = float(input("Digite velocidad vehiculo 2: "))

# proceso de datos
if velocidad_v1 > 0 and velocidad_v2 > 0:
    t = distancia_inicial / (velocidad_v1 + velocidad_v2)
    print(f"\nEl tiempo obtenido es: {t} seg")
else:
    print(f"Error")
