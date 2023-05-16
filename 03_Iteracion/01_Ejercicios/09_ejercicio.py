# 09 Confeccionar un programa que exhiba por pantalla una lista, a dos columnas, con los primeros 15 números impares en la primera y los 15 primeros pares en la segunda, incluyendo los títulos.

print("Números impares   Números pares")
print("----------------  --------------")

for i in range(1, 16):
    num_impar = 2 * i - 1
    num_par = 2 * i
print("{:^16d}  {:^16d}".format(num_impar, num_par))
