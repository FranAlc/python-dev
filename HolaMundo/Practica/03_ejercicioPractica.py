# 03 Ejercicio Gasolinera

# entrada
lt_x_g = float(input("Ingresa los lts por galon: "))
precioxl = float(input("Digite el precio de la gasolina por litro: $"))
consumo = float(input("Digite cuanto sera el consumo del cliente: "))


# proceso
t = consumo * lt_x_g * precioxl

# salida

print("---------------------------------------------")
print("\tEjercicio 3: Gasolinera")
print("---------------------------------------------")
print("Datos de la gosolinera:")
print(f"Consumo: {consumo}lt")
print(f"Precio por Litro: {precioxl}")
print("\nSalida:")
print("-------------------------------------")
print(f"Precio total: ${round(t)+ 1}")
