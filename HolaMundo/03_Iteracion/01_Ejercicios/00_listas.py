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

# Ejercicio 1
# Nombres: almacene los nombres de algunos de sus amigos en una lista llamada nombres. Imprima el nombre de cada persona accediendo a cada elemento de la lista, uno a la vez.

nombres = ["esteban", "martin", "leonel", "facundo"]
message = f"Nombres: {nombres[0].title()}, {nombres[1].title()}, {nombres[2].title()}, {nombres[3].title()}."
print(message)

# Ejercicio 2
# Comience con la lista que usó en el Ejercicio 1, pero en lugar de solo imprimir el nombre de cada persona, imprima un mensaje para ellos. El texto de cada mensaje debe ser el mismo, pero cada mensaje debe estar personalizado con el nombre de la persona.
saludo = f"Hola, {nombres[-4].title()}, como estas?,\nHola, {nombres[-3].title()}, como estas?,\nHola, {nombres[-2].title()}, como estas?,\nHola, {nombres[-1].title()}, como estas?"
print(saludo)

# Ejercicio 3
# Piense en su medio de transporte favorito, como una motocicleta o un automóvil, y haga una lista que almacene varios ejemplos. Use su lista para imprimir una serie de afirmaciones sobre estos elementos, como "Me gustaría tener una motocicleta Honda".
auto = [4, "rojo", "bugatti"]
color = f"El auto es de color {auto[1].title()}"
marca = f"La marca del auto es un {auto[-1].title()}"
cantidad_ruedas = f"La cantidad de ruedas del auto es de {auto[0]}"


print(f"{color},\n{cantidad_ruedas},\n{marca}.")

# Ejercicio 4
# Agregar elementos a una lista desde cero
amigos = []
amigos.append("franco")
amigos.append("ramiro")
amigos.append("facundo")
amigos.append("gonzalo")
amigos.insert(-2, "Federico")
print(amigos)

# Ejercicio 5
# Nombrar a un amigo de la lista con el metodo pop()

ultimo_amigo = (amigos.pop(-1))
nombrar = f"Con el ultimo amigo que hable es {ultimo_amigo.title()}"
print(nombrar)

# Ejercicio 6
# Piensa en al menos tres tipos de tu pizza favorita. Almacene estos nombres de pizza en una lista y luego use un ciclo for para imprimir el nombre de cada pizza.
pizzas = []
pizzas.append("Jamon y queso")
pizzas.append("Morron")
pizzas.append("Basica")
print(pizzas)
for nombre_pizza in pizzas:
    print(f"\nPizza: {nombre_pizza.title()}")
# 6.1 - cada pizza, debe tener una línea de salida que contenga una declaración simple "como Me gusta la pizza de pepperoni".
    print(f"Me gusta la pizza de {nombre_pizza.title()}\n")
print("Me falta comprar un agua!")

# Ejercicio 7
# Piensa en al menos tres animales diferentes. Guarde los nombres de estos animales en una lista y luego use un ciclo for para imprimir el nombre de cada animal.
animales = ["perro", "gato", "loro"]
animales.append("hamster")
for nombra_animales in animales:
    print(f"Nombre:{nombra_animales.title()}")
print("Cualquiera de estos animales seria una gran mascota")

# Ejercicio 8
# Ingresa 4 equipos de futbol que te gusten en una lista (agrega desde afuera de la lista) y luego use un ciclo for para imprimir el nombre de cada uno.

equipos_futbol = ["Boca Junios", "Barcelona", "Milan"]
equipos_futbol.append("Manchester city")
print(f"{equipos_futbol}")
for nombres_equipos in equipos_futbol:
    print(f"Equipo: {nombres_equipos.title()}")

# Ejercicio 9
# usos del ciclo for
cuadrados = [valor**2 for valor in range(1, 11)]
print(f"{cuadrados}")
# Ejercicio 9.1
# Conta hasta 20
numeros = [valor for valor in range(20)]
print(f"{numeros}")
# Ejercicio 9.2
# cuenta de 1 a 100
numeros = [valor for valor in range(1, 100)]
print(f"sum: {sum(numeros)}")  # Suma todos los numeros
print(f"min: {min(numeros)}")  # Muestra el valor menor
print(f"min: {max(numeros)}")  # Muestra el valor mayor
print(f"arreglo: {numeros}")
# Considerar dos posibilidades
numero_par = list(range(2, 11, 2))
print(f"numero par: {numero_par}")

cuadrados = []
for valor in range(2, 11):
    cuadrado = valor ** 2
cuadrados.append(cuadrado)

# Ejercio 9.3
# cuenta numeros impares y pares
# use el tercer argumento de la función range() para hacer una lista de los números impares del 1 al 20. Use un bucle for para imprimir cada número
numero_impar = list(range(1, 20, 2))
print(f"arreglo: {numero_impar}")
for numero in numero_impar:
    print(f"Numero impar:{numero}")
# Ejercicio 9.4
# Haga una lista de los múltiplos de 3 de 3 a 30. Use un ciclo for para imprimir los números en su lista.
numeros_threes = list(range(3, 30, 3))
for numero in numeros_threes:
    print(f"numeros_threes: {numero}")
# Ejercicio 9.5
# El cubo de 2 se escribe como 2**3 en Python. Haga una lista de los primeros 10 cubos (es decir, el cubo de cada número entero del 1 al 10) y use un ciclo for para imprimir el valor de cada cubo.
# lista
cubos = []
for numero in range(1, 11):  # numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # cubo = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3]
    cubo = numero ** 3
    cubos.append(cubo)
for cubo in cubos:
    print(cubo)
# lista de comprension
cubos = [numero ** 3 for numero in range(1, 11)]
print(cubos)
