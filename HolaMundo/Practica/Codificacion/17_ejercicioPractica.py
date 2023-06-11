# 17 Implementar el uso de switcher para los meses del año.

switcher = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

opcion = int(input("Digite un numero de mes: "))
# si muestra el mes seria salida 1
nombre_mes = switcher.get(opcion, "Mes invalido")  # salida 2
print(nombre_mes)
