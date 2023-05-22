# 05 Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:
# paso 1: crea una lista vacía llamada beatles;
# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
# paso 3: emplea el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.

# paso 1:
beatles = []
print("Lista vacia: ", beatles)
# paso 2:
beatles.append("John Lennon")  # 0
beatles.append("Paul McCartney")  # 1
beatles.append("George Harrison")  # 2
print("Primera lista", beatles)

# paso 3:
for i in range(2):
    new_names = input("Ingresa un nombre: ")
    beatles.append(new_names)
print(beatles)
# paso 4:
kik = int(input(
    f"Ingresa en un rango de: {len(beatles)} a quien quieres eliminar: "))
del beatles[kik]
print(f"Lista con usuarios eliminados: {beatles}")

# paso 5:
beatles.insert(0, "Ringo Starr")
print(f"Lista final: {beatles}")
