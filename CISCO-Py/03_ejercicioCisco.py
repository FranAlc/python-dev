# 04 En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:
"""
1.toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
2.si es par, evalúa un nuevo c0 como c0 ÷ 2;
3.de lo contrario, si es impar, evalúe un nuevo  c0  como 3 x c0 + 1;
4.si c0 ≠ 1, salta al punto 2.
La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.
Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.
"""

c0 = int(input("Digite un numero natural: "))
n = 0

while c0 != 1:
    print(c0)

    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1

    n += 1

print(c0)
print(f"Cantidad de pasos para lograr el objetivo: {n}")
