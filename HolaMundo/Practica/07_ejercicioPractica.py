# 07 Si tengo una cantidad de soles, dar su equivalente en dólares y después en euros. Se sabe que 1 dólar =3.25 soles y 1 euro=3.83 soles.

# inicio

# datos
soles_dolar = 3.25
soles_euro = 3.83

# entrada de datos
cant = float(input("Digite la cantidad de soles: $"))

# proceso de datos
dolar = cant * soles_dolar  # dolar = cant/soles_dolar
euro = cant * soles_euro  # euro = cant/soles_euro

# salida de datos
print("-------------------------------------")
print("Ejercicio 7: Soles a Dolar y Euro ")
print("-------------------------------------")
print(f"Dinero ingresado: ${cant}")
print("\nSalida:")
print("-------------------------------------")
print("Precio total Dolar: $", dolar)
print("Precio total Euro: $", euro)
print("-------------------------------------")
