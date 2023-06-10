# 1. Alojamientos de datos.
"""
Listas -> a = [] 


Composicion de una lista: 
elemento:        1          2          3           4         5
jugadores = ['charles', 'martina', 'michael', 'florencia', 'eli']
posición:	     0		   1	       2	       3	     4

Contar cant. elementos/longitud -> len(a)
Contar cant. de veces que x aparece en la lista -> .count("x")

Acceder -> 1.print(a[0]) // 2.print(a[1]) 

Modificar -> a[0]  = "" // print(a) >> [""] #modifica el elemento de la posicion 0

Agregar :
1. .append(nuevoElemento) // 
2. .insert(0,nuevoElemento) #Agrega un nuevo elemento en la posicion 0 // 
3. .extend("hola") >> “h” , “o” , “l” , “a” // 2.Agrega varios elementos a la lista.

Eliminar :
1.del a[0] // Borra el primer elemento de la lista.
2. .pop() // Elimina un elemento de una lista, pide indice y devuelve un valor.
3. .clear() // Elimina todos los elementos.
4. .remove() // Remueve un elemento de una lista, pide valor.

Ordenar -> 1. .sort() #Ordena los elementos de una lista ya sea de manera numérica de menor a mayor o por la inicial del abecedario.
           2. print(sorted(a)) #Ordena la lista pero temporalmente "solo para mostrar como se veria ordenada".
           3. .reverse() #Invierte el orden de una lista.           

Iteracion ->
1.Contar elementos dentro de una lista:
for elementos_lista_a in a:
    print(elementos_lista_a)               
>> []

2.Contar elementos acompañados un indice:
for index, elementos_lista_a in a:
    print(elementos_lista_a)
>>1 elemento
>>2 elemento

3.Zip() -> Iterar dos listas a la vez:
a = [5, 9]
x = ["Rock" , "Pop"] 
for a,x in zip(a,x):
    print(a,x)
>> 5 "Rock"
>> 9 "Pop"    

Adentrar numeros a una lista: 
numeros = list(range(1,6))
print(numeros) 
>>[1, 2, 3, 4, 5]


Sublistas -> x = [1, 2, 3, 4, 5, 6]
            1.print(x[0:3]) >> [1, 2, 3]
            2.print(x[1:3]) >> [2, 3]
Modificar sublistas -> x[0:3] = [0, 0, 0] 
                    1. print(x) >> [0, 0, 0, 4, 5, 6]

"""
