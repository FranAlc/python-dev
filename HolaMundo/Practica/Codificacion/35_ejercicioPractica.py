# Funciones anidadas

def operacion():
    def suma(num1, num2):
        return num1 + num2

    def resta(num1, num2):
        r = num1 - num2
        return r
    print("Suma: ")
    print(suma(10, 20))
    print("Resta:")
    print(resta(60, 20))


operacion()
