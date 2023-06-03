"""
Se ingresa valores positivos entre 1 y 50, finalizando el ingreso con el valor -10, para ello generar una función
que valide dicho ingreso.  ##

Calcular:

a. Cantidad de números pares. ##
b. Promedio de los números impares.

Utilizar las siguientes funciones:
c. Resto: recibe por parámetro el Dividendo y el Divisor; Retorna el resto.
d. EsPar: recibe por parámetro un número; Retorna 1 si es Par, 0 si es Impar; Invoca a la función Resto.
e. Promedio: recibe por parámetro la suma y el contador; Retorna el promedio si contador > 0 sino
Retorna 0.
"""


# funciones


def validar_ingreso_valores_positivos():
    print("Se ingresa valores positivos entre 1 y 50.")
    numero_entre_1_50 = int(input("Valor numerico: "))
    return numero_entre_1_50


def resto(nro, divisor):
    resultado_resto = nro % divisor
    return resultado_resto


def es_par(nro):

    if resto(nro, 2) == 0:
        return 1
    else:
        return 0


# main

contador_pares = 0

acumulador = 0
contador_impares = 0

nro = validar_ingreso_valores_positivos()

while nro != -10:

    if es_par(nro) == 1:
        contador_pares += 1
    else:
        acumulador = acumulador + nro
        contador_impares += 1

    nro = validar_ingreso_valores_positivos()

print("Pares:", contador_pares)

prom = acumulador/contador_impares

print("Promedio impares:", prom)
