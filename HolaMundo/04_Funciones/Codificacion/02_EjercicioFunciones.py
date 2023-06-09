"""
Se ingresan números enteros comprendidos entre 100 y 2000 (usar función LeerYValidar). Determinar
usando la función EstaDentroDelRango:
a. Cantidad de números ingresados entre 100 y 500
b. Cantidad de números pares ingresados entre 500 y 1200
c. Promedio de números ingresados entre 1200 y 2000
El ingreso de datos finaliza cuando se ingresa un número igual a 99.
Para realizar este programa se deben realizar las siguientes funciones:
- EstaDentroDelRango: que reciba 3 enteros correspondientes a un número a validar y los límites
superior e inferior del rango. La función debe retornar un 1 si el número a validar se encuentra
dentro del rango indicado o un 0 si no lo está.
- LeerYValidar: que reciba los límites superior e inferior de un rango y retorne un número que se
encuentre dentro del mismo. (El ingreso de datos se realiza dentro de la función). Para validar el
rango utilizar la función EstaDentroDelRango realizada en el punto anterior

"""

# Datos
# leer_validar
# dentro_rango


def leer_validar():
    print("Digite numeros enteros entre 100 y 2000..")
    i = int(input("\nNumero entero: "))

    if i >= 100 and i <= 2000:
        dentro_rango()

    else:
        print("Finalizo el programa...")


def dentro_rango():
    contador_num_100y500 = 0
    contador_par = 0
    contador_num_1200y2000 = 0

    num = int(input("\nNumero entero: "))
    while num >= 100 and num <= 2000:
        # num (100-500)
        if 100 <= num <= 500:
            contador_num_100y500 += 1

            # num (500-1200)
        elif 501 <= num <= 1200:
            r = (num/2) == 0
            if r != 0:
                contador_par += 1
            else:
                contador_par += 0

            # num (1200-2000)
        if 1201 <= num <= 2000:
            contador_num_1200y2000 += 1
        num = int(input("\nNumero entero: "))

    print("\nNumeros (100-500): ", contador_num_100y500)
    print("Numeros Pares(500-1200): ", contador_num_100y500)
    print("Numeros (1200-2000): ", contador_num_1200y2000)


leer_validar()
