"""
Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
"""


# funciones
def esMultiplo():
    print("Numeros multiplos:")
    resultado_num_multiplo = num % num2 == 0
    return resultado_num_multiplo


# main
print("Digite dos numeros enteros.")
num = int(input("Numero: "))
num2 = int(input("Multiplo: "))
num_multiplo = esMultiplo()
print(num_multiplo)
