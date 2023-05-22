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

# Indexacion de listas
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

# Funciones vs metodos
# Una función no pertenece a ningún dato - obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.
