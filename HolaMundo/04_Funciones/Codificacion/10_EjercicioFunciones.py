"""
Realice un programa que pregunte aleatoriamente una multiplicación. 
El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta). 
"""
import random

# funciones


def indicar_respuesta(resultado):
    resultado_cls = int(input("Digite un resultado: "))
    if resultado_cls == resultado:
        return print("El resultado mensionado es CORRECTO.")
    else:
        print("El resultado mensionado es INCORRECTO.")


# main


num1 = random.randrange(1, 40)
num2 = random.randrange(1, 10)
resultado = num1 * num2
print(f"MULTIPLICACION: {num1} X {num2}")

while num1 != 0:
    indicar_respuesta(resultado)
    print(f"Resultado correcto: {resultado}\n")
    num1 = random.randrange(1, 40)
    num2 = random.randrange(1, 10)
    resultado = num1 * num2
    print(f"MULTIPLICACION: {num1} X {num2}")
