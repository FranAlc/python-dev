# for
# break - ejemplo
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# continue - ejemplo
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

twos = [2 ** i for i in range(8)]

# operadores in y not in

# for i in elemento: print(i) ------> Pregunta si "i" se encuentra dentro de elemento y devuelve True
# for i not in elemento: print(i) ------> Pregunta si "i" falta dentro de elemento y devuelve True

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


# ---------- Indexacion de listas ----------
numbers = [10, 5, 7, 2, 1]
# Imprimiendo contenido de la lista original.
print("Contenido de la lista:", numbers)

numbers[0] = 111
# Contenido actual de la lista.
print("Nuevo contenido de la lista: ", numbers)

numbers = [10, 5, 7, 2, 1]
# Imprimiendo contenido de la lista original.
print("Contenido de la lista original:", numbers)

numbers[0] = 111
# Imprimiendo contenido de la lista anterior.
print("\nPrevio contenido de la lista:", numbers)

# Copiando el valor del quinto elemento al segundo elemento.
numbers[1] = numbers[4]
# Imprimiendo el contenido de la lista actual.
print("Nuevo contenido de la lista:", numbers)

# Ordenar lista de menor a mayor
# lista.sort()

# append() y insert()
# list.append(value)
# list.insert(position, value)
numbers = [1, 2, 3, 4, 5, 6]

print(len(numbers))

numbers.append(7)  # agreggo numero
print(len(numbers))  # cuento cuantos son y muestro en pantalla
print(numbers)

numbers.insert(7, 8)  # agrego numero en la position especificada
print(len(numbers))
print(numbers)

numero = []
# Agregar valores
for i in range(5):
    numero.append(i+1)
print(numero)

# Segunda forma para agregar valores
for i in range(5):
    dato = input("Ingresa un dato a la lista: ")
    numero.append(dato)
print(len(numero))
print(numero)

"""
Ejercicio practico: 
1.crea una lista de un elemento llamada list_1;
2.la asigna a una nueva lista llamada list_2;
3.cambia el único elemento de list_1;
4.imprime la list_2;
"""
# paso 1:
list_1 = [1]
# paso 2:
list_2 = list_1
# paso 3:
list_1[0] = 2
# paso 4:
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# ---- matrices -----

# ---------- Funciones vs metodos ----------
# Una función no pertenece a ningún dato - obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.
