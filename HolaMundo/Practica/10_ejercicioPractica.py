# 10 Realice un programa que convierta millas a kilómetros. Se sabe que una milla equivale a 1.609344 kilómetros.

# inicio
# datos
# entrada de datos
kilometros = 1.609344
cant_milla = float(input("Ingresa la cantidad de millas: "))

# proceso de datos
c = cant_milla * kilometros

# salida
print("-----------------------------------------")
print("Ejercicio 10: Ejercicio de millas a km")
print("-----------------------------------------")
print("Dato ingresado:")
print(f"Cantidad de millas: {cant_milla}")
print("\nSalida:")
print("-------------------------------------")
print(f"Millas: {cant_milla} tiene {c}km")
print("-------------------------------------")
