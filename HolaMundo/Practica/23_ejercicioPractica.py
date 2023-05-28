# 23 Se desea leer por teclado un número comprendido entre 0 y 10 (inclusive) y se desea visualizar si el número es par o impar.

num = float(input("Numero entre 0 y 10: "))

if num <= 10 and num >= 0:
    r = (num % 2) == 0
    if (r == 0):
        print(f"El {round(num)} es par")
    else:
        print(f"El {round(num)} es impar")
else:
    print("El valor no coincide entre 0 y 10.")
