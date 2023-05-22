# 1.0 Escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"
for i in range(1, 6):
    print(i, "Mississippi")
print("¡Listos o no aquí voy!")

## ------------------------------------------------------##

# 2.0 Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.
frase_user = input("ingresa una palabra: ")

while (frase_user != "chupacabra"):

    print("Estas dentro del bucle!")
    frase_user = input("ingresa una palabra: ")
print("Has dejado el bucle con exito.")

## ------------------------------------------------------##


## ------------------------------------------------------##


c0 = int(input("ingresa un numero que no sea negativo y que no sea cero: "))
while c0 > 0 and c0 != 0:

    resultado = c0/2 == 0
    if (resultado != 0):
        print(f"El numero {c0} es par.")
        break
    elif (resultado == 0):
        print(f"{c0} es impar")
        break
c0 = int(input("ingresa un numero que no sea negativo y que no sea cero: "))
