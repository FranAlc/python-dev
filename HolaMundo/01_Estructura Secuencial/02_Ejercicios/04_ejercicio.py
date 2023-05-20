# 04 Confeccionar un programa que ingrese una medida en ‘pies’ y la exhiba convertida a yardas, pulgadas, cms. y mts. NOTA: 1 pie = 12 pulgadas; 1 yarda = 3 pies; 1 pulgada = 2,54 cms

medida_pie = float(input("Ingresa la medida de tu pie: "))

yardas_pie = medida_pie / 3.0
pulgadas = medida_pie * 12.0
centimetros = pulgadas * 2.54
metros = centimetros / 100.0

print(f"la medida de tu pie {medida_pie}, son equivalentes a:")
print(f"yardas: {yardas_pie} ")
print(f"pulgadas: {pulgadas}")
print(f"centímetros: {centimetros}")
print(f"metros: {metros}")
