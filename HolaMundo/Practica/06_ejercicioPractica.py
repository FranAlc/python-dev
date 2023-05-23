# 06 Ejercicio, Triángulo equilatero , pedir altura y mostrar el perimetro

# Entrada de datos
altura = float(input("Ingresa altura del triangulo: "))

# Proceso de datos
perimetro = 3*(2*altura/3**0.5)

# Salida de datos
print("-------------------------------------")
print("Ejercicio 6: Triangulo equilatero")
print("-------------------------------------")
print("Datos ingresado:")
print(f"Altura: {round(altura)}")
print("\nSalida:")
print("-------------------------------------")
print("Perimetro del triangulo: {}".format(perimetro))
