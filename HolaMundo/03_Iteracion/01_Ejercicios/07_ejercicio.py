"""
07 Dadas 20 notas y legajos de alumnos de un curso. Determinar:
a. Cantidad de alumnos aplazados.
b. Cuando la nota sea mayor o igual a 7, mostrar el mensaje: “El alumno con legajo xxx ha Promocionado”.
"""

cant_notas = 20
cant_alumnos_aplazados = 0

for i in range(1, cant_notas+1):
    nota = int(input(f"{i}-Ingresa tu nota:"))
    if nota >= 7:
        print(f"El alumno con legajo {nota} ha Promocionado\n")
    else:
        print(f"El alumno con legajo {nota} ha Desaprobado\n")
        cant_alumnos_aplazados += 1

print(f"La cantidad de alumnos aplazados son: {cant_alumnos_aplazados}")
