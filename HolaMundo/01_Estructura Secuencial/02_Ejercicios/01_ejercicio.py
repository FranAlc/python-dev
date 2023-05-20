# 01_ Se ingresan la cantidad de horas trabajadas y el valor por hora de un empleado. Determinar el sueldo.

# Ingresar cantidad de horas trabajadas y valor por hora
cantidad_horas_trabajadas = float(
    input("Ingresar la cantidad de horas trabajadas: "))
valor_hora = float(
    input("Ingresar el valor que obtienes por hora de trabajo: "))
# Multiplicar cantidad de horas trabajadas por valor por hora
resultado_sueldo = cantidad_horas_trabajadas * valor_hora
# Mostrar resultado
print("El sueldo determinado es: $", resultado_sueldo)
