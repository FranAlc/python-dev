# Matrices
"""
#TEORIA: Matrices
cuenta -> numero_filas * numero_columnas = dimension de la matriz

Los elementos de este arreglo son objetos matematicos:
1. Numeros enteros
2. Numeros reales
3. Valores logicos
4. Cadenas

Tipos de matrices:
a) matriz = [[0,0,0], [0,0,0]] #Matriz nula
b) matriz = [[1,2,3]] #Matriz fila
c) matriz = [[1],[2],[3]] #Matriz columna -> *1 , 2 , 3 en forma de columna*.
d) matriz = [[1, 2, 3], [3, 4, 5], [6, 7, 8]] #Matriz en forma cuadrada.
e) matriz = [[1, 2, 3, 4],[5, 6, 7, 8]] #Matriz en forma rectangular.

Traza de una matriz = 1 + 4 + 8 #La suma de los elementos en diagonal, tome como referencia el punto d) de arriba.
Diagonal secundaria = 3 + 4 + 6 #La suma de los elementos en la diagonal secundaria.
Matriz unidad = Su diagonal es de 1 [[1,0,0], [0,1,0], [0,0,1]]

------------------------------------------------------------------------------------------------
Estructura -> 1. matriz = [[1,2],[3,4]] 2x2 // 2. matriz = [[1,2],[3,4],[5,6]] 3x2 filasXcolumnas 

#Sistemas:

Mostrar elemetentos de una matriz -> 1. m[[0],[1],[2]] // 2. m[[1,2,3],[4,5,6],[7,8,9]] -> [[0,1,2], [0,1,2], [0,1,2]]

Acceso directo -> m = [[0, 1, 2], [3, 4, 5]] -> mostrar= m[0][2] >> 2 #Mostraria en concreto el elemento seleccionado

Recorrer la lista completa -> m = [[0, 1, 2], [3, 4, 5]] -> mostrar= m[0:2] >>  [[0, 1, 2], [3, 4, 5]] #Comienza de cero y recorre hasta el "elemento 2"
[1,3] -> recorre desde la posicion 1 y va hasta el tercer elemento.



"""
