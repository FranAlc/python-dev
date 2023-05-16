# 04 Se ingresan 10 letras. Determinar la cantidad de vocales ingresadas.
letras = input("Ingresa 10 letras: \n")
cantidad_vocales = 0

for letra in letras:
    if letra.lower() in 'aeiouAEIOU':
        cantidad_vocales += 1

print(f"La cantidad de vocales mencionadas es: {cantidad_vocales}")
