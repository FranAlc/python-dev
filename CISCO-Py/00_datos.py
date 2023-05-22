"""
# break - ejemplo
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# continue - ejemplo
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
"""
c0 = int(input("ingresa un numero que no sea negativo y que no sea cero: "))
while c0 > 0 and c0 != 0:

    resultado = c0/2 == 0
    if (resultado == 0):
        print(f"El numero {c0} es par")

    elif (resultado != 0):
        print(f"El numero {c0} es impar")

    c0 = int(input("ingresa un numero que no sea negativo y que no sea cero: "))
