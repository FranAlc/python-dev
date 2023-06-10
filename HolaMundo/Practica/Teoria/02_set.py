# 2. Alojamientos de datos.
"""
Conjuntos.
set = ([]) // {1,2,3} or {"h",2,3}

#Los elementos de un set son unico, no se pueden duplicar.
#Elementos sin orden.
#Elementos inmutables.

Crear set -> 1. x = set([1, 2, 3]) //2. x = {1,2,3}

Contar cant. elementos/longitud -> len(x)
Elemento presente o no -> print("2" in x) >>True

Comparar conjuntos -> 1. a | b #Muestra los dos conjuntos .
                      #Muestra que datos se repiten en los dos conjuntos ( a= {1,2,3} b= {0,5,3} >> {3} )
                      2. a & b
                      3. a - b #Diferencia , que valores no estan uno del otro.

Agregar -> .add(2) #Añade un elemento con el valor de 2.

Eliminar -> 1) .remove() #Elimina el elemento que se pasa como parámetro, si no se encuentra lanza la excepcion KeyError. // 
            2) .discard() #Elimina el elemento que se pasa como parámetro, y si no se encuentra no hace nada.
            3) .pop() #Elimina un elemento random, no espera argumento.
            4) .clear() #Elimina todos los elementos.

"""
