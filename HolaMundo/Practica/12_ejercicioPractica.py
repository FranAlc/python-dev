# 12 Dado la velocidad de 2 cuerpos que se dirigen uno al encuentro de otro determinar el tiempo de encuentro si la distancia que los separa inicialmente es “D”.

# inicio
# datos
# entrada de datos
va = float(input("Ingresa la velocidad del primer cuerpo: "))
vb = float(input("Ingresa la velocidad del segundo cuerpo: "))
distancia = float(input("Digite la distancia que los separa: "))
tiempo = 0

# proceso de datos
tiempo = distancia/(va + vb)

# salida
print("------------------------------------------------")
print("Ejercicio 12: Ejercicio tiempo de encuentro")
print("------------------------------------------------")
print("Datos ingresados:")
print(f"Velocidad A: {vb}")
print(f"Velocidad B: {vb}")
print(f"Distancia: {distancia}")
print("\nSalida:")
print("------------------------------------------------")
print(f"Tiempo: {tiempo} segundos")
print("------------------------------------------------")
