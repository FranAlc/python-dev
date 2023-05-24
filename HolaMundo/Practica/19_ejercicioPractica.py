# 19 Dado el sueldo de un trabajador, aplique un aumento del 15% si su sueldo es inferior a $1000. Imprima el sueldo que percibirá.

# inicio
# entrada de datos
aumento = 0
sueldo = float(input("Digite su sueldo: $"))

# proceso de datos

if sueldo < 1000:
    # salida 1
    aumento = sueldo * 0.15
    sueldo += aumento
    print("-------------------------------")
    print(f"Tu sueldo final es: ${sueldo}")
    print("-------------------------------")
elif sueldo >= 1000:
    # salida 2
    print("-------------------------------")
    print("Tu sueldo es mayor o igual a $1000")
    print(f"Tu sueldo final es: ${sueldo}")
    print("-------------------------------")
