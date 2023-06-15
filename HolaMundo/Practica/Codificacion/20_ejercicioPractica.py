# 20 Desarrolle un algoritmo para determinar si un año leído por teclado es o no bisiesto.
import math
# Inicio
# entrada de datos
anio = int(input("Digite un anio: "))
bisiesto = 0

# proceso de datos

if (anio % 4 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
    # salida
    print("----------------------------")
    print(f"Su año {anio} es bisiesto")
    print("----------------------------")
else:
    # salida 2
    print("------------------------------")
    print(f"El año {anio} no es bisiesto")
    print("------------------------------")
