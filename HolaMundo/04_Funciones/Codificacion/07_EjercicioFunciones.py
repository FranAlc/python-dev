"""
Programa que toma las tres notas de un estudiante y diga la nota final del curso.
"""
# funciones


def promedio_final():
    promedio = acumulador / 3
    return promedio


def desaprueba_aprueba():
    if (promedio >= 7):
        return print("Aprobo.")
    else:
        return print("Desaprobo.")


# main
acumulador = 0
print("Digite las 3 notas de un estudiante.")
for i in range(1, 4):
    nota = int(input(f"{i}.Digite nota:"))
    acumulador += nota

promedio = promedio_final()
desaprueba_aprueba()
