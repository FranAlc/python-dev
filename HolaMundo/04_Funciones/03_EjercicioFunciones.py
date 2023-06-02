"""
Se realizó un concurso de tiro al blanco. Por cada participante se ingresa un número que lo identifica y el
resultado de los disparos efectuados. El ingreso finaliza con un número de participante negativo.
Cada participante efectúa 5 disparos, registrándose las coordenadas X-Y de cada disparo.

- No considere disparos sobre los ejes, pero sí en el centro (si es sobre los ejes las coordenadas
deberán volver a ingresarse).
- Para determinar el cuadrante utilizar la función CUADRANTE que reciba las dos coordenadas y
retorne el cuadrante al cual pertenece (1 a 4) y 0 para indicar un tiro en el centro.

Para calcular el puntaje utilizar la función PUNTAJE que reciba 5 parámetros que representan la cantidad
disparos en cada cuadrante y en el centro. La función debe retornar el puntaje obtenido según la siguiente
escala:
- Cuadrantes 1 y 2: 50 puntos
- Cuadrantes 3 y 4: 40 puntos
- Centro: 100 puntos

Determinar:
a. El puntaje obtenido por cada participante, detallando cuantos disparos realizó en cada cuadrante.
b. Mostrar el número del participante ganador y el puntaje obtenido.
c. Calcular y mostrar la cantidad total de disparos en el centro (de todos los participantes)
"""


# FUNCIONES
def repeticion_disparo():
    print("1- Numerico.")
    print("2- Ejes")
    opcion = int(input("Digite una opcion: "))
    if (opcion == 1):
        puntaje_numerico()
    elif (opcion == 2):
        repeticion_disparo()


def puntaje_numerico():
    cuadrante_1_2 = 50
    cuadrante_3_4 = 40
    centro = 100

    for i in range(1, 6):
        numerico = int(input("\nNumero: "))
        if numerico == 1:
            cuadrante_1_2 += 1
    print(f"Puntuacion: {numerico}")


def cuadrante():
    print("1- Numerico.")
    print("2- Ejes")
    opcion = int(input("Digite una opcion: "))
    if (opcion == 1):
        puntaje_numerico()
    elif (opcion == 2):
        repeticion_disparo()
    else:
        print("tiro afuera")


# main
print("\n----------------------------")
print("CONCURSO DE TIRO AL BLANCO")
print("----------------------------")
print("Cuadrantes 1 y 2: 50 puntos")
print("Cuadrantes 3 y 4: 40 puntos")
print("Centro: 100\n")
print("\t-")
print("\t-")
print("   2    -    1")
print("\t-")
print("--------0--------")
print("\t- ")
print("   3    -    4")
print("\t-")
print("\t-")

participante = int(input("Digite el numero que lo identifica: "))

while participante >= 1:
    cuadrante()
    print(f"Participante: #{participante}")
    participante = int(input("Digite el numero que lo identifica: "))
print("\nFin del programa.")
