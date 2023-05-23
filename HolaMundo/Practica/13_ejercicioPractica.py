# 13 Dado un ángulo en Radianes conviértalo a grados Sexagesimales y luego a Centesimales.


pi = 3.1416
radianes = float(input("Digite los radianes: "))

convert_sexa = radianes*180/pi
convert_cen = radianes*200/pi

print("\n-------------------------------------------")
print("Salida:")
print("Convertido en sexagesimal: ", convert_sexa)
print("Convertido en centesimal: ", convert_cen)
