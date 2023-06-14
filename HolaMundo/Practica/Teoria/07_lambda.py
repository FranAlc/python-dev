"""
Lambda -> #lambda se muestra mejor cuando los usa como una función anonima dentro de otra funcion.
          #Utilizar funciones lambda cuando se requiera una función anonima durante un breve período de tiempo.
Fuera de una funcion -> x = lambda a,b : a + b
Dentro de una funcion -> return / yield lambda a : a + (parametro de la funcion)

Diferencias: 1. Lambda -> agregar_uno = lambda x : x + 1
             2. def -> def agregar_uno(x) : return x + 1

Funcion anonima -> (lambda x, y: x + y)(2, 3) >> 5 
#La función lambda anterior se define y luego se llama inmediatamente con dos argumentos (2 y 3). 
#Devuelve el valor 5, que es la suma de los argumentos.
             
"""
