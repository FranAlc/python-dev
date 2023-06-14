# 1. Tipos de errores.
# Anotacion de los siguientes errores que se presentan en un programa
"""
NameError -> 1. Usar sin declarar una variable. // 2. Caso incorrecto, error tipografico // 3. Usar sin importar una funcion externa.
ZeroDivisionError -> Se genera al dividir por cero. Dividir por 0 diverge infinitamente, por lo que la computadora no puede devolver un valor.
IndexError -> Ocurre al extraer un elemento de un objeto iterable. Entrada de índice incorrecta.
TypeError -> Operador. Ocurre cuando el metodo no coincide con el tipo requerido. Cuando arg no se inserta en la llamada de funcion.
KeyError -> Cuando no hay una clave correspondiente en el dict.
ModuleNotFoundError -> Cuando no existe un modulo con ese nombre. Se debe comprobar si hay errores tipograficos o asegurarse de que el directorio este bien // Tal vez el entorno virtual esta mal.
"""

# 2. Anotacion de "vectores".
"""
Listas -> Mutables // Quiere decir que se puede -> 1.Modificar elementos // 2.Agregar elementos // 3.Eliminar elementos // 4.Organizar elementos
Tuplas ->  Inmutables
Diccionarios -> Mutables

3. Operadores:
Comparacion -> == , != , >, >=, <, <=
Identidad -> is, is not
Membresia -> in, not in
bit -> &, |, ^, <<, >>

4. Iteradores
__iter__(): Devuelve un objeto iterador.
__next__(): 1. Devuelve el siguiente valor para el iterable.
            2. Cuando usamos un bucle for para atravesar cualquier objeto iterable, internamente usa el método iter() para obtener un objeto iterador.
for -> 1. for x,a in d: //2. for x,a in zip(x,a) //range()

"""
