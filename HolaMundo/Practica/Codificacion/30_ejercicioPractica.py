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
print(f"\n{mensaje}")

# DICCIONARIOS
diccionario = {}
diccionario = dict()

# {llave : el valor de el cual queremos asociar. }

diccionario = {"total": 66}
diccionario = {"total": 66, "descuento": True, "subtotal": 15}
usuario = {
    "nombre": "Franco",
    "apellido": "Galan",
    "edad": 20,
    "skills": {
        "Programacion": True,
        "DB": True
    },
    "cursos": ["CISCO", "Codigo facilito", "Python Data Science IBM"]
}

# AGREGAR elementos a nuestro diccionario
elementos = {}  # si se duplican las llaves se añade solo el ultimo valor asignado

elementos['nombre'] = "Daniel"
elementos[(1, 2, 3)] = "la llave es una tupla"
elementos['nombre'] = "Franco"  # actualiza el nombre
print(elementos)

# cuenta la cantidad de elementos dentro de nuestro diccionario
print(len(elementos))

# elementos , obtener valores
dicc = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
valor = dicc['d']
print(valor)
print('b' in dicc)  # muestra si se encuentra 'b' devolviendo True o False

if 'a' in dicc:  # declara si se encuentra o no un elemento dentro del diccionario
    print(f"Existe 'a' y su valor es: {dicc['a']}")
else:
    print("No se encuentra")

# get
# en caso que no se encuentre devuelve None
valor = dicc.get('d')
print("valor:", valor)
# setdefault
# en caso que no exista , la crea y añade con el valor escrito
valor = dicc.setdefault('e', 5)
print("valor:", valor)


# Llaves, items y valores
# keys
user = {'nombre': 'franco', 'apellido': 'galan'}
key = user.keys()
print("key:", key)  # muestra los elementos dentro de una lista

key = tuple(user.keys())  # puedo convertirlo en tupla o en lista
print("key:", key)
key = list(user.keys())  # lista
print("key:", key)
# values
valores = tuple(user.values())
print("valores:", valores)
# elementos
elementos = tuple(user.items())
print("elementos:", elementos)

# ELIMINAR elementos
# ingresar la llave del elemento que deseo eliminar
user = {'nombre': 'franco', 'apellido': 'galan'}
# 1 del
del user['apellido']
print("user:", user)  # borra apellido
print(len(user))
# 2 pop()
# valor = user.pop('b')
# print("pop:", valor)
# 3 metodo clear
user.clear()  # borra todos los elementos del diccionario user{}


# Condicionales - Ternario

calificacion = 10
color = None

if calificacion >= 7:
    color = "verde"
else:
    color = "rojo"
print(calificacion)
print(color)

color = 'verde' if calificacion >= 7 else "rojo"


# Funciones

def suma():
    num = int(input("numero: "))
    num2 = int(input("numero: "))
    r = num + num2
    return print(r)


suma()

# usar variables de afuera de la funcion


def resta(num1, num3):
    r = num1 - num3
    return print(r)


num1 = int(input("numero: "))
num3 = int(input("numero: "))
resta(num1, num3)

# def area_circulo(radio,pi = 3.14) >> los parametros con valores se encuentran a la derecha y no a la izquierda sino devuelve un error


def area_circulo(radio, pi):
    # retorna una tupla , se recomienda un max de 3 valores
    return pi * (radio**2), "este es el area de un circulo"


radio = int(input("radio: "))
pi = 3.1416

imprimir_resultado = area_circulo(radio, pi)  # >>retorna los dos valores

# imprimir_resultado, mensaje = area_circulo(radio, pi) >> retorna los dos valores pero se puede extraer un valor en una variable, pasarla de tupla a lista y modificarla si se lo desea
# mensaje = (area_circulo(radio, pi)) >> retorna solamente el mensaje y no el resultado de (pi * radio^2)

# imprimir_resultado, _ = area_circulo(radio, pi) >> retorna solamente el resultado de (pi * radio^2) y no el mensaje ya que se coloco un _

#imprimir_resultado = area_circulo(pi=3.14,radio=10) >> se pueden dar vuelta los parametros con sus respectivos valores

print(imprimir_resultado)
# print(mensaje)
