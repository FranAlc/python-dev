"""
Realizar un programa que al ingresar solicite el ingreso de dos números enteros y luego muestre por
pantalla el siguiente menú (las xx de los números deben ser reemplazadas con los valores
correspondientes):

Menú de Opciones
---- -- --------
Numero 1: xx Numero 2: xx
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
Ingrese su opción:
Al ingresar el número de la opción del 1 al 4, se realiza la operación y muestra el resultado hasta que se
presione una tecla. Luego vuelve a mostrar el menú para poder realizar otra operación con los mismos
números. 
El ingreso de la opción debe estar validado y en caso de ingresarse un número no válido se cierra el programa.
Usar una función para mostrar el menú y retornar el valor elegido
"""

# Declaro funciones


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def denegar():
    return print("No se reconoce el numero ingresado")


def programa():
    print("\n - - - - - - - - - - - - -")
    print("\t Menu de opciones")
    print("1- SUMAR")
    print("2- RESTAR")
    print("3- MULTIPLICAR")
    print("4- DIVIDIR")
    opcion = int(input("\nDigite una opcion: "))
    while (opcion <= 4 and opcion >= 1):
        if opcion == 1:
            sumar = suma(num1, num2)
            print("\nRESPUESTA:")
            print("Suma: ", sumar)

        elif opcion == 2:
            restar = resta(num1, num2)
            print("\nRESPUESTA:")
            print("Resta: ", restar)

        elif opcion == 3:
            multiplicar = multiplicacion(num1, num2)
            print("\nRESPUESTA:")
            print("Multiplicacion: ", multiplicar)
        elif opcion == 4:
            dividir = resta(num1, num2)
            print("\nRESPUESTA:")
            print("Dividision: ", dividir)
        else:
            print(denegar())

        print("\n - - - - - - - - - - - - -")
        print("\t Menu de opciones")
        print("1- SUMAR")
        print("2- RESTAR")
        print("3- MULTIPLICAR")
        print("4- DIVIDIR")

        opcion = int(input("\nDigite una opcion: "))


num1 = int(input("Digite un numero entero: "))
num2 = int(input("Digite un segundo numero entero: "))

programa()

print("\nFin del programa.")
