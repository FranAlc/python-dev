# 25 Algoritmo, que dado dos números enteros "a", "b" y "c", integrarlos a una lista llamada numeros y luego muestre sus valores en orden de menor a mayor.

numeros = []
# entrada de datos
a = int(input("Numero: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))
numeros.append(a)
numeros.append(b)
numeros.append(c)

# muestra datos agregados sin ordenarlos de mayor a menor
print("\nLista normal:")
print(numeros)

# ordena los datos

print("\nLista de menor a mayor:")
numeros.sort()
print(numeros)

# salida
print("\nPresiona una tecla para salir...")
input()
