# 10 Una pizzería vende empanadas por unidad o por docena, la docena cuesta $300 pero si se compra  individualmente se cobra $30 la unidad. Si se compran más empanadas que no se agrupen en docenas las adicionales se cobran como por unidad. Indicar el precio total a abonar.

num_empanadas = int(input("Ingrese la cantidad de empanadas a comprar: "))

precio_unitario = 30
precio_docena = 300
docenas = num_empanadas // 12
individuales = num_empanadas % 12

precio_total = (docenas * precio_docena) + (individuales * precio_unitario)

print("El precio total a abonar es de $", precio_total)
