# Main
import personajes
import enemigos
from enemigos import *
from personajes import *

# funcion de datos del guerrero

"""
def personaje_guerrero():
    personaje = Guerrero()

    print("Digite los datos del guerrero:")
    nombre_personaje = input("Nombre: ")
    estatura_personaje = float(input("Estatura: "))
    arma_personaje = input("Ingrese un arma: ")
    fuerza_personaje = int(input("Fuerza: "))

    # alojar datos anteriores
    personaje.nombre = nombre_personaje
    personaje.estatura = estatura_personaje
    personaje.tipo_arma = arma_personaje
    personaje.fuerza = fuerza_personaje
    personaje.atributos()


personaje_guerrero()
"""
# resto del main
print("Digite contra quien desea pelear: ")
opcion_pelea = input("Dragon(Drg) // Monstruo(Monst): ")
change_minus = opcion_pelea.lower()  # converti en minuscula la opcion
while change_minus == "monst" or change_minus == "drg":
    print("Dentro del bucle")
    if change_minus == "monst":
        personaje = Guerrero()
        print(f"Guerrero {personaje.nombre}")
        print("Seleccionaste pelear con un Monstruo.\n")
        enemigo = Monstruos()
        enemigo.atributos()

    elif change_minus == "drg":
        print("Todavia no desarrollado.")
        print("Digite otra opcion.")

    # fin del bucle
    print("\nDigite contra quien desea pelear: ")
    opcion_pelea = input("Dragon(Drg) // Monstruo(Monst): ")
    change_minus = opcion_pelea.lower()

print("\nENEMIGO NO ENCONTRADO..")
