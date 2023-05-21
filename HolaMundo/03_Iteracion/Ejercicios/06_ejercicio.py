"""
06 
    Ingresar N y N Números naturales. Determinar e informar:
a. La sumatoria de los valores múltiplos de 3.
b. La cantidad de valores múltiplos de 5.
c. La sumatoria de los valores que se ingresan en orden par.

"""

n = int(input("Ingrese la cantidad de números naturales a ingresar: "))

sumatoria_multiplos_3 = 0
cantidad_multiplos_5 = 0
sumatoria_pares = 0

for i in range(n):
    numero = int(input("Ingrese un número natural: "))

    if numero % 3 == 0:
        sumatoria_multiplos_3 += numero

    if numero % 5 == 0:
        cantidad_multiplos_5 += 1

    if i % 2 == 0:
        sumatoria_pares += numero

print(
    f"a. La sumatoria de los valores múltiplos de 3 es: {sumatoria_multiplos_3}")
print(f"b. La cantidad de valores múltiplos de 5 es: {cantidad_multiplos_5}")
print(
    f"c. La sumatoria de los valores ingresados en orden par es:  {sumatoria_pares}")
