# 31 crear funciones las cuales puedan recibir una n cantidad de argumentos
# crear una funcion que me permita calcular el promedio de un listado de numeros enteros

def promedio(listado):
    # obtener la suma total de todos los elementos dentro de una tupla o lista
    return sum(listado) / len(listado)


resultado = promedio([10, 10, 5, 7, 10])
print(resultado)

# 1.
# resultado = promedio(10, 10, 5, 7, 10) >> devuelve un error ya que la funcion promedio unicamente toma un argumento "listado" y no varios como (10, 10, 5, 7, 10)
# 2.SOLUCION
# resultado = promedio(10, 10, 5, 7, 10) >> se le agrega al parametro de la funcion (*listado), el '*' logra que el programa devuelva una tupla
# se recomienda nombrar a este parametro como (*args)
