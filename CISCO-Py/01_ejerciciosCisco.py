# 1.0 Escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"
for i in range(1, 6):
    print(i, "Mississippi")
print("¡Listos o no aquí voy!")

# 2.0 Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.
frase_user = input("ingresa una palabra: ")

while (frase_user != "chupacabra"):

    print("Estas dentro del bucle!")
    frase_user = input("ingresa una palabra: ")
print("Has dejado el bucle con exito.")

# 3.0 Tu programa debe:
"""
Pedir al usuario que ingrese una palabra.
utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada
Prueba tu programa con los datos que le proporcionamos.
"""

palabra = input("Ingresa una palabra: ")  # ingresa palabra
print(palabra.upper())  # convertir palabra ingresada a mayuscula

resultado = ""
for letra in palabra:
    if letra.upper() in ['A', 'E', 'I', 'O', 'U']:
        continue  # Salta a la siguiente iteración del bucle si es una vocal
    resultado += letra
print("Letras vocales consumidas : ", letra)
