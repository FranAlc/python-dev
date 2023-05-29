# Practica de listas
lista = [5, 6, 8, 20, 892, 95, 6, 9, 478, 10, 88, 2, 1]
lista.sort()

print(f"Numero menor: {lista[0]}")
print(f"Numero mayor: {lista[-1]}")

# segunda forma:
print(f"Numero menor: {min(lista)}")
print(f"Numero menor: {max(lista)}")

# encontrar dentro de una lista
if 10 in lista:
    print("10 esta en lista.")
else:
    print("10 no esta en lista.")
# se puede negar con el operador logico not
if 10 not in lista:
    print("10 no esta en lista.")
else:
    print("10 esta en lista.")

# encontrar el indice de un elemento si es que se encuentra.

if 10 in lista:
    print("10 esta en lista.")
    # si hay varios elementos 10, mostrara en consola solo el primero que encuentre
    index = lista.index(10)
    print(f"posicion: {index}")
else:
    print("10 no esta en lista.")

# Matrices.
columna_a = [10, 20]
columna_b = [30, 40]

matriz = [columna_a, columna_b]  # matriz 2 x 2

print(f"\n{matriz}")
print(matriz[1][1])
"""   0  1
    0[10 20]
    1[30 40]
"""

columna_a = [10, 20, 42, 60]  # 2 x 4
columna_b = [30, 40, 50, 63]
lista = [columna_a, columna_b]
#                y  x
print(f"\n{lista[0][2]}")


# Mostrar lista como tupla
lista = ["Franco", "Programador", 20]

datos = tuple(lista)

print(f"\n{datos}")  # lista pasa a ser una tupla

tupla = ("Dia", "Noche", "Tarde")

datos = list(tupla)  # tupla pasa a ser una lista y se puede modificar

print(f"\n{datos}")

num = int(input("Digite un numero: "))
datos.append(num)

print(f"\n{datos}")

# ZIP

lista = [1, 2, 3, 4, 5]
lista2 = [100, 200, 300, 400, 500]
tupla = (10, 20, 30, 40, 50)

resultado = zip(tupla, lista, lista2)
resultado = tuple(resultado)
print(f"\n{resultado}")
print(resultado[0][2:])

# Strings con listados
lenguajes = 'Python-Javascript-C-C++'
listado_lenguajes = lenguajes.split("-")

print(listado_lenguajes)

lenguajes = ["Python", "Javascript", "C++", "Java"]

string_lenguajes = ' '.join(lenguajes)
print(string_lenguajes)

# justificar texto
mensaje = "Hola mundo!"
mensaje = mensaje.ljust(20)  # Alinear a la izquierda
print(f"\n{mensaje}.")

mensaje = mensaje.rjust(20)  # Alinear a la Derecha
print(f"\n.{mensaje}")

# Centrar "-----Hola Mundo!-----" 5 de un lado y 5 del otro
mensaje = mensaje.center(10)
print(f"\n-{mensaje}-")
