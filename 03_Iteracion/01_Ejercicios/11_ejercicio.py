"""
11 Realizar un programa que:
a. Muestre todos los números primos entre 1 y 100. (Un nro. es primo cuando es divisible solamente
por 1 y por sí mismo)
b. Contar y mostrar la cantidad de primos encontrados.
"""
cantidad_primos = 0

for numero in range(1, 100 + 1):
    es_primo = True
    if numero < 2:
        es_primo = False
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
    if es_primo:
        cantidad_primos += 1
        print(numero)

print("La cantidad de números primos encontrados es:", cantidad_primos)
