# Main
import personajes
import enemigos
from enemigos import *
from personajes import *

# llamado de las clases localmente
personaje = Guerrero()
enemigo = Monstruos()


def bienvenida_al_personaje():
    print("\n-------------------------------------------------------------------------------------------")
    print(f"HOLA {personaje.nombre.upper()}, BIENVENIDO A ESTA AVENTURA.")
    print(
        f"PARA COMENZAR RECUERDE QUE SU VIDA ES DE {personaje.vida} y su fuerza es {personaje.fuerza} .")
    print(f"TENIENDO EN CUENTA ESO A LA HORA DE PELEAR SU FUERZA ES EL ATAQUE QUE INFLIGE AL ENEMIGO.")
    print(f"¡ BUENA SUERTE !")


# funcion de datos del guerrero
def personaje_guerrero():
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


print("\n\t--------¡ JUEGO DE AVENTURA !--------\n")
print("Usted sera un personaje y debera luchar contra un enemigo...\n")
personaje_guerrero()
bienvenida_al_personaje()
# resto del main

print("Digite contra quien desea pelear: ")
opcion_pelea = input("Dragon(Drg) // Monstruo(Monst): ")
change_minus = opcion_pelea.lower()  # converti en minuscula la opcion
while change_minus == "monst" or change_minus == "drg":
    print("Dentro del bucle")
    if change_minus == "monst":
        print(f"Guerrero {personaje.nombre}")
        print("Seleccionaste pelear con un Monstruo.\n")

        enemigo.atributos()

    elif change_minus == "drg":
        print("Todavia no desarrollado.")
        print("Digite otra opcion.")

    # fin del bucle
    print("\nDigite contra quien desea pelear: ")
    opcion_pelea = input("Dragon(Drg) // Monstruo(Monst): ")
    change_minus = opcion_pelea.lower()

print("\nENEMIGO NO ENCONTRADO..")
