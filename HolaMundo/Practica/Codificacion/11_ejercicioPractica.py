# 11 Si se conoce la longitud de dos de los lados de un triángulo (b y c) y el ángulo entre ellos (alfa), expresado en grados sexagesimales, la longitud del tercer lado (a) se calcula por la formula:
# a^2 = b^2 + c^2 – 2bc*cos(alfa)

# inicio
import math
# datos
pi = 3.1416
r = float(0)
# entrada de datos
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))
alfa = float(input("Ingrese el ángulo en grados sexagesimales: "))
# proceso de datos
r = alfa*pi/180
a = (b**2 + c**2 - 2*b*c*math.cos(r)) ** 0.5
# salida
print("------------------------------------------------")
print("Ejercicio 11: Ejercicio de lados de un triangulo")
print("------------------------------------------------")
print("Datos ingresados:")
print(f"b: {b}")
print(f"c: {c}")
print(f"alfa: {alfa}")
print("\nSalida:")
print("------------------------------------------------")
print(f"El resultado total de A es: {a}")
print("------------------------------------------------")
