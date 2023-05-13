# 07 Se ingresa un número entero que representa una fecha con formato (ddmmaa). Se pide transformarlo a un número con formato (aammdd).
fecha = int(input("Ingrese una fecha con formato ddmmaa: "))

# Extraer las unidades y decenas de día, mes y año
dia_unidades = fecha % 10
dia_decenas = (fecha // 10) % 10
mes_unidades = (fecha // 100) % 10
mes_decenas = (fecha // 1000) % 10
anio_unidades = (fecha // 10000) % 10
anio_decenas = fecha // 100000

# Construir el número entero con formato (aammdd)
nueva_fecha = (anio_decenas * 1000) + (anio_unidades * 100) + (mes_decenas *
                                                               10) + mes_unidades + (dia_decenas * 10000) + (dia_unidades * 1000)

# Mostrar el resultado
print("La fecha ingresada con formato aammdd es:", nueva_fecha)
