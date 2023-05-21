# 07 Confeccionar un programa que solicite e ingrese 3 valores reales positivos, mayores que cero y determine e informe si forman o no triángulo. Para ello utilizar el teorema de la desigualdad del triángulo que establece que la suma de las longitudes de cualesquiera de dos lados de un triángulo es mayor que la longitud del tercer lado.
a = float(input("Ingrese el valor del primer lado: "))
b = float(input("Ingrese el valor del segundo lado: "))
c = float(input("Ingrese el valor del tercer lado: "))

if a > 0 and b > 0 and c > 0:  # Verificar que los lados sean positivos y mayores que cero
    # Verificar si se cumple la desigualdad del triángulo
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Los lados ingresados forman un triángulo.")
    else:
        print("Los lados ingresados no forman un triángulo.")
else:
    print("Los lados deben ser valores reales positivos y mayores que cero.")
