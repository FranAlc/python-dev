"""
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena 
con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “.
Crea un programa principal donde se use dicha función.
"""

# funcion


def convertir_espaciado(texto):
    cadenaTransformada = " ".join(texto)
    return print(cadenaTransformada)


# main
texto = "Hola, tú."
convertir_espaciado(texto)
