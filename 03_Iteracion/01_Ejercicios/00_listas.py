# Range() genera una secuencia // (2 donde empieza , 11 donde termina, 2 tamaño de paso al generar números)
for valor in range(2, 11, 2):  # va de 2 en 2
    print(valor)
for valor in range(1, 5):  # "0, 1, 2, 3, 4, 5"
    print(valor)

# Si se coloca Range() dentro de un list() te los guarda en una lista
numero = list(range(1, 5))  # [0, 1, 2, 3, 4, 5]
print(numero)

# Uso de listas
# 1.0 Cortar una lista
jugadores = ["charles", "martina", "martin", "franco", "facundo"]
print(jugadores[0:3])  # [posicion:elemento] o [elemento:] o [:elemento]

# 1.1 Copiar una lista
lista_nombres1 = ["mario", "miguel", "franco", "mauro", "facundo"]
lista_nombres2 = ["antonella", "maria", "malena", "javier", "leo"]
print(lista_nombres1)
print(lista_nombres2)
lista_nombres1.append("mateo")
print(lista_nombres1)
"""
temperaturas = []
for i in range(18):
    temperatura = float(input("Ingrese el valor de temperatura: "))
    temperaturas.append(temperatura)
"""
"""
alumnos = []
for i in range(10):
    alumno = str(input(f"{i})Ingresa el nombre de cada alumno:"))
    alumnos.append(alumno.title())
print(alumnos)
"""

"""
numero = int(input("Numero: "))
mensaje = str(input("mensaje: "))

for i in range(0, numero):
    print("{} {}".format(i, mensaje))
"""

# Estructura de datos:
# -Listas
lista = list()  # lista = []
print(type(lista))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', True, False]
print(len(lista))

# pop() Borra posicion de una lista
# del lista[1] Borra perma
# append() agrega elementos a una lista

# -Tuplas

# -Diccionarios
