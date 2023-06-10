# 08 Dado el tiempo en segundos y la distancia en metros de un movil, ingresados por teclado, calcule la velocidad correspondiente.

# inicio
# datos
# entrada de datos
tiempo = float(input("Ingresa el tiempo en segundos: "))
dist = float(input("Ingresa la Distancia en metros: "))

# proceso de datos
velocidad = dist/tiempo

# salida
print("-------------------------------------")
print("Ejercicio 8: Velocidad de un movil ")
print("-------------------------------------")
print("Datos ingresados:")
print(f"Tiempo en segundos: {tiempo}")
print(f"Distancia en metros: {dist}")
print("\nSalida:")
print("-------------------------------------")
print(f"La velocidad es: {velocidad} m/s")
print("-------------------------------------")
