# 10 Solicita dos numeros por teclado y realiza las siguientes comparaciones:
"""
- Son iguales , distintos, es menor A que B , es mayor A que B, A es mayor o igual que B, A es mayor o igual que B.
"""
# Solicitar dos números al usuario
num_a = float(input("Ingrese el primer número: "))
num_b = float(input("Ingrese el segundo número: "))

# Comparar los números
if num_a == num_b:
    print("Los números son iguales.")
else:
    print("Los números son distintos.")
    if num_a < num_b:
        print("El número A es menor que el número B.")
    else:
        print("El número A es mayor o igual que el número B.")
        if num_a > num_b:
            print("El número A es mayor que el número B.")
        else:
            print("El número A es igual al número B.")
