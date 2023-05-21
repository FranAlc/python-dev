# 09 Confeccionar un programa que permita ingresar un caracter alfanumerico y determine e informe si lo ingresado corresponde a una vocal, con el mensaje “VOCAL”. y su correspondiente valor numérico en ASCII.
caracter = input("Ingrese un carácter alfanumérico: ")

if len(caracter) == 1:  # Verificar que se haya ingresado un solo carácter
    if caracter in "AEIOUaeiou":  # Verifica si el carácter ingresado es una vocal
        print("VOCAL")
    else:
        print("NO VOCAL")
    # Imprimir el valor numérico en ASCII del carácter ingresado
    print("Valor en ASCII: ", ord(caracter))
else:
    print("Debe ingresar un solo carácter alfanumérico.")
