"""
08 Dadas las edades y estaturas de 45 alumnos de un curso. Determinar:
a. Edad promedio.
b. Estatura promedio.
c. Cantidad de alumnos mayores o iguales a 10 años.
d. Cantidad de alumnos que miden menos de 1.40 cm.
"""
alumnos_curso = 10
cant_alumnos_mayores = 0
cant_alumnos_estatura = 0


for i in range(1, alumnos_curso+1):
    print(f"\nAlumno {i}:")
    # edad
    edad = int(input("Ingresar tu edad: "))
    if edad >= 10:
        print("Eres mayor")
        cant_alumnos_mayores += 1

        if edad < 10 and edad > 8:
            print("Eres menor")
    else:
        print("No tienes la edad indicada")

    # estatura
    estatura = float(input("Ingresa tu estatura: "))
    if estatura >= 1.40:
        print("Eres de estatura alta - promedio")
    if estatura < 1.40:
        print("Eres de estatura baja al promedio")
        cant_alumnos_estatura += 1

print(
    f"\nLa cantidad de alumnos mayores o iguales a 10 años: {cant_alumnos_mayores}")
print(
    f"La cantidad de alumnos que miden menos de 1.40 cm: {cant_alumnos_mayores}")
