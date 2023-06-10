# 09 Calcular el monto a pagar por un artículo si se tiene como datos de entrada la cantidad de docenas que compra y el costo por unidad de este artículo.

# inicio
# datos
# entrada de datos

articulo = float(input("Ingresa monto a pagar por un artículo: $"))
cant_docenas = float(input("Ingresa el numero de docenas: "))

# proceso de datos
monto = articulo * 12 * cant_docenas

if monto > 0:

    # salida
    print("-----------------------------------------")
    print("Ejercicio 9: Ejercicio de monto a pagar")
    print("-----------------------------------------")
    print("Dato ingresado:")
    print(f"Articulo: ${articulo}")
    print(f"Cantidad de docenas: {round(cant_docenas)}")
    print("\nSalida:")
    print("-------------------------------------")
    print(f"El monto total es: ${monto}")
    print("-------------------------------------")

elif monto == 0:
    monto2 = articulo * 12
    # salida 2
    print("-----------------------------------------")
    print("Ejercicio 9: Ejercicio de monto a pagar")
    print("-----------------------------------------")
    print("Dato ingresado:")
    print(f"Articulo: ${articulo}")
    print(f"Cantidad de docenas: {round(cant_docenas)}")
    print("\nSalida:")
    print("-------------------------------------")
    print(f"El monto total es: ${monto2}")
    print("-------------------------------------")

else:
    # salida 3
    print("-------------------------------------")
    print("No se aceptan numeros negativos")
    print("-------------------------------------")
