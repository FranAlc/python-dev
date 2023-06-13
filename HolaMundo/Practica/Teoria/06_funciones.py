"""
#FUNCIONES -> def function(argumentos): codigo return(retorno)

Algunos principios del uso de funciones:
-Una funcion siempre debe devolver un valor.
-Verificar que la cantidad de parametros con que invocamos la funcion son los mismos que se definieron al momento de crear la funcion.
-Evitar el codigo repetido para realizar una funcion que mantenga por unica vez dicho codigo para luego solo llamarlo.
-Modularidad, en vez de hacer largos trozos de codigo, es mejor modulos o funciones que agrupen ciertos fragmentos de codigo en funciones especificas.

Llamar una funcion ->
def saludar():
    print("Hola, me llamo Franco")

saludar() #Esto invoca la funcion saludo y devuelve aquello dentro de la funcion >> Hola, me llamo Franco
    
Llamar una funcion con una variable ->
def suma():
    a= 5
    b= 10
    r = a + b
    return r >>15
sumar = suma()
print(sumar) #En este caso,la variable sumar toma como dato suma() la cual debe mostrar en consola su proceso.

Uso de parametros ->
1. def saludar(nombre) #parametro 'nombre'
    print(f"Hola {nombre}, como estas?")

saludar("Manuel") #Se debe pasar como entrada un nombre

2. def saludar(nombre, apellido): #2 parametros
    print(f"Hola {nombre} {apellido}, como estas?")

saludar("Franco") #En este caso al ser 2 parametros se deben devolver 2 valores y no solo 1. >> Devuelve un error
______
#A la hora de tener que ingresar el valor de los parametros de una funcion se puede -> 1. a=20, b=10 // 2. variable, variable2 //3. "nombre", "apellido"
______

Argumentos por defecto -> def suma(a,b=0): return a+b // suma(5+6) or suma (5) #Ya que ve tiene un valor por defecto saldria 0 salvo que se indique lo contrario.

2. def suma(a=3, b=5, c=0):
    return a+b+c
suma() >> 8
suma(4,5) >> 9
suma(5,3,2) >> 10

Parametro tupla -> def suma(*numeros) -> suma(1, 5, 6) 
Parametro lista -> def suma(numeros) > suma([1, 5, 6])


"""
