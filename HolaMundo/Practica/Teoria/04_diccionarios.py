# 4. Alojamientos de datos.
"""
Diccionarios / dict-> (key/value)  -> dict{'nombre': 'Franco'}

Modificar elementos -> 1.x.get('nombre')= "Daniel"  / 2.x['nombre'] = "Daniel"


Imprimir un diccionario -> 1. for i in x: print(i) // 
                           2. for j in x: print(x[j]) #Imprime el valor
                           3. for i, j in x : print(i,j) #Imprime el elemento como el valor
                           4. k = x.keys() >> dict_keys(['a', 'b']) #Devuelve una lista con todas las keys del diccionario.
                           4.1 k = x.keys() // print(list(k)) >> ['', ''] #Devuelve una lista
                           5. x.values() #Devuelve solo los valores de las keys


Anidar un diccionario -> x = {} // d = {}
                        anidar{
                            "diccionario1" : x
                            "diccionario2" : d
                        }
                        print(anidar) >> {"diccionario1" : {x} , "diccionario2" : {d}}

Agregar elementos-> x['nombre'] = "Daniel"
                    x[(1, 2, 3)] = "la llave es una tupla"
                    x['nombre'] = "Franco"  # actualiza el nombre
                    print(x) 

Cambiar los valores de las keys y esta ultima no esta es añadida -> 1. x = {} d = {} // 2 .x = x.update(d)


Eliminar elementos-> .clear() #Eliminar todo el contenido
                     .pop() #Elimina un elemento de un dict, pide nombre de la key.
                     .popitem() #Elimina de forma aleatoria

Cuenta la cant. de elementos: print(len(x)) 

Saber si se encuentra o no un elemento en un diccionario -> 1. print("hola" in x) // 2. if "hola" in x:return .. else ..
                                                            3. x.get('nombre') // 4. print(x.get('nombre', 'no encontrado')) >> 'no encontrado'

Devolver una lista con keys y values -> 1. it = x.items() >>dict_items([('', 1), ('', 2)]) //2. print(list(it)) >>[('', 1), ('', 2)]

"""
