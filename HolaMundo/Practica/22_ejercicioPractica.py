import math
# 22 Dado un entero no negativo x, devuelve la raíz cuadrada de x redondeada al entero inferior más cercano . El entero devuelto tampoco debe ser negativo .

x = float(input("numero no negativo: "))

if x > 0:
    r = math.sqrt(x)
    if r > 0:
        print(f"El valor de x redondeado: {round(r - 1)}")
    elif r < 0:
        print("El resultado no puede ser menor a cero.")
else:
    print("No se aceptan valores negativos")
