# 02 Tu programa debe:
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
print("Letras vocales consumidas : ", letra.upper())
