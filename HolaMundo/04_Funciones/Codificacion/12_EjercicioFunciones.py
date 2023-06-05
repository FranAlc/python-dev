"""
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente. 
La función preguntará al usuario el valor y la función a aplicar, 
y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""


# funciones

def triangulo():
    print("    *")
    print("    **")
    print("    ***")
    print(" C.O****")
    print("    ***** H")
    print("    ******")
    print("    *******")
    print("      C.A")


def calculadora_menu(opcion):

    if opcion == 1:  # seno
        sen = seno(angulo_co, hipotenusa)
        print("--------RESPUESTA----------")
        print(f"El numero SENO es: {sen:2}")

    elif opcion == 2:  # coseno
        cos = coseno(angulo_ca, hipotenusa)
        print("--------RESPUESTA----------")
        print(f"El numero COSENO es: {cos:2}")

    elif opcion == 3:  # tangente
        tan = coseno(angulo_co, angulo_ca)
        print("--------RESPUESTA----------")
        print(f"El numero COSENO es: {tan:2}")
    elif opcion == 4:  # los 3
        sen = seno(angulo_co, hipotenusa)
        cos = coseno(angulo_ca, hipotenusa)
        tan = coseno(angulo_co, angulo_ca)
        print("--------RESPUESTA----------")
        print(f"El resultado de SENO es: {sen:2}")
        print(f"El resultado de COSENO es: {cos:2}")
        print(f"El resultado de TANGENTE es: {tan:2}")
    else:
        print("Opcion no valida.")
# sen = c.o / h


def seno(angulo_co, hipotenusa):
    sen = angulo_co / hipotenusa
    return sen

# cos = c.a / h


def coseno(angulo_ca, hipotenusa):
    cos = angulo_ca / hipotenusa
    return cos

# tan = c.o / c.a


def tangente(angulo_co, angulo_ca):
    tan = angulo_co / angulo_ca
    return tan


# main
bucle = 1

while bucle > 0:

    print("----------menu-opciones-----------")
    print("1.Seno")
    print("2.Coseno")
    print("3.Tangente")
    print("4. Los 3 al mismo tiempo")
    print("----------------------------------")
    triangulo()
    opcion = int(input("Digite una opcion: "))
    print("")
    angulo_co = float(input("Cateto opuesto: "))
    angulo_ca = float(input("Cateto adyacente: "))
    hipotenusa = float(input("Digite Hiponenusa: "))

    calculadora_menu(opcion)
    print("\nPARA FINALIZAR MARQUE UNA OPCION? 0.Si")
