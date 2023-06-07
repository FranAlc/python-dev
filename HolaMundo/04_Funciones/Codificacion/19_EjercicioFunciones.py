"""
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"
"""

# funcion


def inversa(cadena_str):
    # [posicion:elemento:recorre]
    cadena_inversa = cadena_str[::-1]
    print(cadena_inversa)


# main
palabra = "estoy probando"
inversa(palabra)
