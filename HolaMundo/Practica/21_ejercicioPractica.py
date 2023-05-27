import random
print("\n*********************PARTIDO DE FUTBOL**************************")
print("---------------------------PENALES--------------------------------")
# datos
jugadores1 = []
jugadores2 = []
penales1 = []
penales2 = []

# entrada de datos
print("Digite el nombre de su club: ")
equipo_futbol1 = str(input("\nEQUIPO 1: "))
equipo_futbol2 = str(input("\nEQUIPO 2: "))

# entrada de nombre de jugadores
print(f"\n{equipo_futbol1.title()}")
for i in range(1, 6):
    nombre_jugador = str(input(f"{i}.JUGADOR: "))
    jugadores1.append(nombre_jugador.title())
arquero = str(input("6.ARQUERO: "))
jugadores1.append(arquero.title())

# entrada de nombres de jugadores 2
print(f"\n{equipo_futbol2.title()}")
for i in range(1, 6):
    nombre_jugador2 = str(input(f"{i}.JUGADOR: "))
    jugadores2.append(nombre_jugador2.title())
arquero2 = str(input("6.ARQUERO: "))
jugadores2.append(arquero2.title())


# equipo 1
print("\nLista de jugadores:")
print(f"{equipo_futbol1.title()}")
for nombres in jugadores1:
    print(f"JUGADOR: {nombres.title()}.")

# equipo 2
print("\nLista de jugadores:")
print(f"{equipo_futbol2.title()}")
for nombres2 in jugadores2:
    print(f"JUGADOR: {nombres2.title()}.")

# penales empieza pateando
patea = [equipo_futbol1.title(), equipo_futbol2.title()]
start = random.choice(patea)

print(f"\nComienza pateando: {start}")

pelota = ["Golazo", "Atajo el arquero", "Pego en el palo"]

if start == patea[0]:
    # equipo 1
    print(f"Primer penal pateado por: {jugadores1[0]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales1.append(resultado)
    # equipo 2
    print(f"\nPrimer penal pateado por: {jugadores2[0]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales2.append(resultado)
    # equipo 1
    print(f"\nSegundo penal pateado por: {jugadores1[1]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales1.append(resultado)

    # equipo 2
    print(f"\nSegundo penal pateado por: {jugadores2[1]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales2.append(resultado)

    # equipo 1
    print(f"\nTercer penal pateado por: {jugadores1[2]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales1.append(resultado)

    # equipo 2
    print(f"\nTercer penal pateado por: {jugadores2[2]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales2.append(resultado)
    # equipo 1
    print(f"\nCuarto penal pateado por: {jugadores1[3]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales1.append(resultado)
    # equipo 2
    print(f"\nCuarto penal pateado por: {jugadores2[3]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales2.append(resultado)

    # contar la cantidad de goles
    cantidad_goles1 = penales1.count("Golazo")

    cantidad_goles2 = penales2.count("Golazo")

    if cantidad_goles1 > cantidad_goles2:
        print("\nFIN TANDA DE PENALES:")
        print(f"{equipo_futbol1.title()} : {penales1}")
        print(f"\n{equipo_futbol2.title()} : {penales2}")
        print("\n*************************************")
        print(f"\tCAMPEON : {equipo_futbol1} !!!")
        print("***************************************")
    elif cantidad_goles2 > cantidad_goles1:
        print("\nFIN TANDA DE PENALES:")
        print(f"{equipo_futbol1.title()} : {penales1}")
        print(f"{equipo_futbol2.title()} : {penales2}")
        print("\n**************************************")
        print(f"\tCAMPEON : {equipo_futbol2.title()} !!!")
        print("***************************************")
    elif cantidad_goles1 == cantidad_goles2:
        # equipo 1
        print(f"\nQuinto penal pateado por: {jugadores1[4]}")
        resultado = random.choice(pelota)
        print(f"Resultado: {resultado}")
        penales1.append(resultado)
        # equipo 2
        print(f"\nQuinto penal pateado por: {jugadores2[4]}")
        resultado = random.choice(pelota)
        print(f"Resultado: {resultado}")
        penales2.append(resultado)

        # contar la cantidad de goles
        if cantidad_goles1 > cantidad_goles2:
            print("\nFIN TANDA DE PENALES:")
            print(f"{equipo_futbol1.title()} : {penales1}")
            print(f"\n{equipo_futbol2.title()} : {penales2}")
            print("\n*************************************")
            print(f"\tCAMPEON : {equipo_futbol1.title()} !!!")
            print("***************************************")

        elif cantidad_goles2 > cantidad_goles1:
            print("\nFIN TANDA DE PENALES:")
            print(f"{equipo_futbol1.title()} : {penales1}")
            print(f"\n{equipo_futbol2.title()} : {penales2}")
            print("\n*************************************")
            print(f"\tCAMPEON : {equipo_futbol2.title()} !!!")
            print("***************************************")

elif start == patea[1]:
    # equipo 1
    print(f"Primer penal pateado por: {jugadores2[0]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales1.append(resultado)
    # equipo 2
    print(f"\nPrimer penal pateado por: {jugadores1[0]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales2.append(resultado)
    # equipo 1
    print(f"\nSegundo penal pateado por: {jugadores2[1]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales1.append(resultado)

    # equipo 2
    print(f"\nSegundo penal pateado por: {jugadores1[1]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales2.append(resultado)

    # equipo 1
    print(f"\nTercer penal pateado por: {jugadores2[2]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales1.append(resultado)

    # equipo 2
    print(f"\nTercer penal pateado por: {jugadores1[2]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales2.append(resultado)

    # equipo 1
    print(f"\nCuarto penal pateado por: {jugadores2[3]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales1.append(resultado)

    # equipo 2
    print(f"\nCuarto penal pateado por: {jugadores1[3]}")
    resultado = random.choice(pelota)
    print(f"Resultado: {resultado}")
    penales2.append(resultado)

    # contar la cantidad de goles
    cantidad_goles1 = penales1.count("Golazo")

    cantidad_goles2 = penales2.count("Golazo")

    if cantidad_goles1 > cantidad_goles2:
        print("\nFIN TANDA DE PENALES:")
        print(f"{equipo_futbol1.title()} : {penales2}")
        print(f"\n{equipo_futbol2.title()} : {penales1}")
        print("\n*************************************")
        print(f"\tCAMPEON : {equipo_futbol1.title()} !!!")
        print("***************************************")
    elif cantidad_goles2 > cantidad_goles1:
        print("\nFIN TANDA DE PENALES:")
        print(f"{equipo_futbol1.title()} : {penales2}")
        print(f"\n{equipo_futbol2.title()} : {penales1}")
        print("\n****************************************")
        print(f"\tCAMPEON : {equipo_futbol2.title()} !!!")
        print("******************************************")
    elif cantidad_goles1 == cantidad_goles2:
        # equipo 1
        print(f"\nQuinto penal pateado por: {jugadores2[4]}")
        resultado = random.choice(pelota)
        print(f"Resultado: {resultado}")
        penales1.append(resultado)
        # equipo 2
        print(f"\nQuinto penal pateado por: {jugadores1[4]}")
        resultado = random.choice(pelota)
        print(f"Resultado: {resultado}")
        penales2.append(resultado)

        # contar la cantidad de goles
        if cantidad_goles2 > cantidad_goles1:
            print("\nFIN TANDA DE PENALES:")
            print(f"{equipo_futbol1.title()} : {penales2}")
            print(f"\n{equipo_futbol2.title()} : {penales1}")
            print("\n*************************************")
            print(f"\tCAMPEON : {equipo_futbol2.title()} !!!")
            print("************************************")

        elif cantidad_goles1 > cantidad_goles2:
            print("\nFIN TANDA DE PENALES:")
            print(f"{equipo_futbol1.title()} : {penales2}")
            print(f"\n{equipo_futbol2.title()} : {penales1}")
            print("\n*************************************")
            print(f"\tCAMPEON : {equipo_futbol1.title()} !!!")
            print("************************************")
