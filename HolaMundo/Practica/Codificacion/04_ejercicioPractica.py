# 04 Ejercicio CILINDRO

# entrada
radio = float(input("Ingresa el radio: "))
altura = float(input("Ingresa la altura: "))
pi = 3.1416
# proceso
area = pi * radio ** 2 * altura  # pi * radio ^ 2 * altura
volumen = 2 * pi * radio * (radio + altura)

# salida
print("---------------------------------------------")
print("\tEjercicio 4: CILINDRO")
print("---------------------------------------------")
print("Datos del cilindro:")
print(f"Altura: {round(altura)}")
print(f"Radio:{round(radio)}")
print("\nSalida:")
print("-------------------------------------")
print("Area: {}".format(area))
print("Volumen: {}".format(volumen))
