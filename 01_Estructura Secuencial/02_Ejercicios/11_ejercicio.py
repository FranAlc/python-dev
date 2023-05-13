# 11 Una farmacia vende algunos artículos sin descuento y a otros con descuento del 20%. Confeccionar un programa que recibiendo el precio original y un código que indica si es o no con descuento, informe el precio final (0 no aplica el descuento y 1 aplica el descuento).

precio_articulo = float(input("Ingresa el precio del articulo: "))
codigo = int(input("Ingresa codigo: "))
descuento = (precio_articulo * 20/100) * codigo
total = precio_articulo - descuento

print("Valor total: $", total)
