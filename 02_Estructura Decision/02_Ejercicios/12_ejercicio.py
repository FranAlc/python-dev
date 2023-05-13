"""
12 Ingresar el valor de la hora y la cantidad de horas trabajadas por un empleado. Calcular su sueldo tomando
en cuenta que recibe un premio de $500 si trabajo más de 50 horas y, además, si trabajó más de 150 horas
se le otorgan $1000 adicionales.
"""
horas_trabajadas = int(input("Ingresa las horas trabajadas: "))
valor_hora = int(input("Ingresa el valor x hora: "))

if horas_trabajadas >= 50:
    sueldo_premio_quinientos = (horas_trabajadas * valor_hora) + 500
    print(f"Tu sueldo final es: ${sueldo_premio_quinientos}")

elif horas_trabajadas >= 150:
    sueldo_premio_mil = (horas_trabajadas * valor_hora) + 1000
    print(f"Tu sueldo final es: ${sueldo_premio_mil}")

else:
    sueldo_basico = horas_trabajadas * valor_hora
    print(f"Tu sueldo final es: ${sueldo_basico}")
