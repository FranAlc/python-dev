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
