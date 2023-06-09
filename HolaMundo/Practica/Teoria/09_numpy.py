"""
#Numpy -> import numpy as np -> "np" tomaria el uso de numpy por el resto del archivo

1. Potente estructuras de datos.
2. Implementa matrices y matrices multidimensionales.
3. Estas estructuras garantizan calculos eficientes con matrices.

#Matriz 2x2
matriz = np.array([1,2],[3,4]) 
>> [[1 2]
    [3 4]]  

#Matriz 2x3
matriz = np.array([1,2,3],[4,5,6])
>> [[1 2 3]
    [4 5 6]]    

Definir un vector utilizando una lista -> vector = [1,2,3]

Definir un vector utilizando un array numpy -> vector = np.array([1,2,3])

Definir un vector columna -> vector = np.array([1],[2],[3])

Crear una variable que contenga valores del 0 al 9 -> a = np.arange(10)

Crear arreglo multidimensional -> a = np.array([[1, 2], [3, 4]])
#Shape -> forma >> print(a.shape) >> (2, 2)
#size -> tamaño >> print(a.size) >> 4

Convertir un vector en una matriz -> 2x5 -> 1.Crear un vector // 2.Convertir dicho vector en matriz 2x5
#1.Crear
    a = np.arange(1, 11)
#2.Convertir
    c = a.reshape(2,5) #Guardo en una variable C a la variable A convertida
    print(c)
#3. Convertir 2
    print(a.reshape(2,5)) #Muestro sin guardar en una variable C a la variable A

reshape -> Solo funciona si el numero de elementos del arreglo previo y el final son iguales, en caso que no se cumpla da error. "ValueError"   

Crear vector con numeracion ascendente o descendente -> arange(valor_inicial, valor_final, incremento)
#    vector = arange(-2, 10, 3)
    >> [-2, 1, 4, 7 ]

Por que el uso de Numpy? 
Para cumplir el uso de matrices y no de una forma lenta de procesarlas como lo es implementar las Listas, numpy
cumple con el objetivo de propocionar un objeto de matriz que es hasta 50 veces mas rapido que las listas tradicionales aca en Python.

El objeto matriz de Numpy se llama -> ndarray

Esta biblioteca se utiliza mayormente para la ciencia de datos.


"""