# 08 Confeccionar un programa que ingrese un valor expresado en Kibibyte (KiB) y lo informe expresado en:  TiB, GiB, MiB, con leyendas aclaratorias. (1MiB = 1024 KiB; 1GiB = 1024 MiB; 1TiB = 1024 GiB)

valor_kib = float(input("Ingrese el valor en Kibibyte (KiB): "))

valor_mib = valor_kib / 1024
valor_gib = valor_mib / 1024
valor_tib = valor_gib / 1024

print("El valor ingresado equivale a:")
print(valor_tib, "TiB")
print(valor_gib, "GiB")
print(valor_mib, "MiB")
