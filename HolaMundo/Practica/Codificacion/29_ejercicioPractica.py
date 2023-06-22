# 29. Calcule las raíces reales, de una ecuación de segundo grado.
# La forma de una ecuación de segundo grado es Ax2 + Bx + C,
# para este caso se debe tener presente el valor de la
# discriminante. Para el algoritmo se procede a calcular las
# raíces solo si la discriminante es mayor a CERO

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))


discriminante = b**2 - 4*a*c


if discriminante > 0:
    x1 = ((-b) + discriminante**0.5) / 2*a
    x2 = ((-b) - discriminante**0.5) / 2*a
    print("\nDatos ingresados: ")
    print(f"\nValor a: {a}")
    print(f"\nValor b: {b}")
    print(f"\nValor c: {c}")
    print(f"Respuesta : {x1}, {x2}")
else:
    print("Error, Raices Irracionales")
