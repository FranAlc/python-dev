# 10 Ingresar 18 valores de temperatura distintos de cero. Se pide determinar e informar cuantas ternas (tres valores seguidos) de valores positivos y cuantas de negativos hay.
ternas_positivas = 0
ternas_negativas = 0

temperaturas = []
for i in range(18):
    temperatura = float(input("Ingrese el valor de temperatura: "))
    temperaturas.append(temperatura)

for i in range(len(temperaturas) - 2):
    if temperaturas[i] > 0 and temperaturas[i+1] > 0 and temperaturas[i+2] > 0:
        ternas_positivas += 1
    elif temperaturas[i] < 0 and temperaturas[i+1] < 0 and temperaturas[i+2] < 0:
        ternas_negativas += 1

print("Cantidad de ternas positivas:", ternas_positivas)
print("Cantidad de ternas negativas:", ternas_negativas)
