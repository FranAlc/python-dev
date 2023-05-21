# 05 Confeccionar un programa para calcular la suma de los primeros N números naturales. El valor de N lo solicita por teclado el programa.
n = int(input("Ingrese un número entero positivo: "))

suma = n * (n + 1) // 2  # No es necesario usar un bucle

print(f"La suma de los primeros {n} números naturales es: {suma}")
