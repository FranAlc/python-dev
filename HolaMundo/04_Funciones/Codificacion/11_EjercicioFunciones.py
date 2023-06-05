"""
Escribir una función que aplique un descuento del 25% a un precio y otra que aplique el IVA a un precio.
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, 
y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta
y devolver el precio final de la cesta.
"""

# funciones


def descuento(precio_producto):
    resultado_descuento = precio_producto * 0.25
    resultado_final_desc = precio_producto - resultado_descuento
    return resultado_final_desc


def iva(descuento_25):
    descuento_iva = descuento_25 * 1.21
    descuento_iva_total = descuento_25 + descuento_iva
    return descuento_iva_total


def precios(producto, precio_producto):
    diccionario_precios = {producto, precio_producto}
    return diccionario_precios


# main
comenzar_programar = 1


while comenzar_programar > 0:
    producto = input("Digite que va a comprar: ")
    precio_producto = float(input("Digite el valor de lo que va a comprar: $"))
    # diccionario - producto , precio
    diccionario_de_compra = precios(producto, precio_producto)
    print(diccionario_de_compra)

    # descuento del 25%
    descuento_25 = descuento(precio_producto)
    print(f"El descuento a su producto: {descuento_25}")

    # incremento iva
    precio_final = iva(descuento_25)
    print(f"Precio final: ${precio_final}")

    comenzar_programar = int(
        input("Digite 0 para finalizar o 1 para continuar:"))

print("El programa finalizo..")
