# 02 Ejercicio bases de un triangulo

# entrada
base_rectangulo = float(input("Ingresa la base del rectangulo: "))
altura_rectangulo = float(input("Ingresa la Altura del rectangulo: "))

# proceso
sup = base_rectangulo * altura_rectangulo
per = 2*(base_rectangulo+altura_rectangulo)

# salida
print("---------------------------------------------")
print("Ejercicio 2: Calcular perimetro y superficie")
print("---------------------------------------------")
print("Datos del rectangulo:")
print(f"Base: {base_rectangulo}")
print(f"Altura: {altura_rectangulo}")
print("\nSalida:")
print("-------------------------------------")
print("Superficie: {}".format(sup))
print("Perimetro: {}\n".format(per))
