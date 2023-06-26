# Scope
# 1
animal = "Leon"  # Variable global >> funcion, condicion o ciclo


def imprimir_animal():
    # animal = "Tortuga" >> Variable local >> devolveria el valor "Tortuga" y no el valor de la variable global
    print(animal)


imprimir_animal()
print(animal)

# 2
animal = "Leon"  # Variable global


def imprimir_animal():
    global animal  # >> toma la variable global y modifica su valor
    animal = "Tortuga"  # Variable local
    print(animal)


imprimir_animal()
print(animal)
