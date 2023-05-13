# 12 Solicitar por teclado dos numeros diferentes de cero y realizarles las siguientes operaciones: suma , resta , division, multiplicacion, obtener el modulo o residuo

num = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un segundo numero: "))

if (num != 0) & (num2 != 0) | (num > 0) & (num2 > 0):
    suma = num + num2
    resta = num - num2
    division = num // num2
    multiplicar = num * num2
    modulo = num % num2

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    if (num2 <= 0):
        print(f"No se puede dividir por {num2}")
    else:
        print(f"Tu resultado de division es: {division} ")
    print(f"Multiplicacion: {multiplicar}")
    print(f"Modulo: {modulo}")
else:
    print("No se aceptan valores iguales o menores a cero")
