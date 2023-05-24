# 18 Construir un programa, tal que dado como dato la calificación de un alumno, escriba “aprobado” en caso de que esa calificación sea mayor a 10.

# inicio
# entrada de datos
calif = int(input("Digite su calificacion: "))

# proceso de datos
if calif >= 10:
    # salida 1
    print("------------------------")
    print("El alumno esta aprobado")
    print("------------------------")
else:
    # salida 2
    print("---------------------------")
    print("El alumno esta desaprobado")
    print("---------------------------")
