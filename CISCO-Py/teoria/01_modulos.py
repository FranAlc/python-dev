"""
Teoria:
Manejo de modulos -> 
# 1. Uso de modulos ya existentes - creados por otra persona o por el mismo programador,
# 2. Crear un nuevo modulo, ya sea de uso propio o facilitar el desarrollo de un programa para x persona.
(bibliotecas)

Cada modulo consta de entidades. Estas entidades pueden ser funciones,variables, constantes, clases y objetos. 
Si se sabe como acceder a un modulo en particular, se puede utilizar cualquiera de las entidades que almacena.

funciones matematicas -> nombres del modulo -> (math)
Para llamar a un modulo como "math" se debe importar -> import math
se puede importar la cantidad de modulos que hagan falta.

#siempre uno bajo del otro
import math
import sys
#o enumerando los modulos despues de la palabra clave reservada import
import math,sys

ejemplo:
import math
print(math.sin(math.pi/2))
>> 1.0

Se habilitan los nombres de pi y sin con el nombre de su modulo de origen:
math.pi
math.sin

ejemplo:
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))
>> 0.99
>> 1.0

Segundo modulo: (from)

#La palabra clave reservada from
#Nombre del modulo a ser importado
#Palabra clave reservada import

"""