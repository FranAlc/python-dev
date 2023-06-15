"""
CLASES - OBJETOS
Pilares basicos: 1.Herencia//2.Cohesión//3.Abstraccion//4.Polimorfismo//5.Acoplamiento//6.Encapsulamiento

- Clase -> Diseño. (molde - plantilla)

- Objeto -> Instancia de una clase --> Ejecucion ( MEMORIA )

Componentes de una clase POO -> 1.Atributos // 2.Propiedades // 3. Metodos .
1.Atributos -> 1.Los datos que manejo en una clase. // 2.Nombre y tipo de dato. // 3.Variable privada .
2.Propiedades -> 1.Bloque de codigo {}, que definen el acceso a los atributos. // 2.Nombre y tipo de dato. // 3.get y set.
3.Metodos -> 1.Bloques de codigo, publicos, que pueden tener parametros y definen el comportamiento de la Clase. //Funciones - Procedimientos
Funcion -> retorna un valor // Procedimientos -> no retorna un valor

Python en POO se comporta siguiendo estos pasos: 
1.
#Atributos de clase. -> Atributos que pertenecen a una clase
class Usuario:
    username = ""

Usuario.username = "Franco"
print(Usuario.username)

2.
#Atributos de instancia. 
class Usuario:
    username = ""

user1 = Usuario()
print(user1.username)

Llamar a un atributo de clase : 1. Usuario.username = "Franco" //
                                2. user1 = Usuario() >> user1.username = "Franco" >>print(user1.username)

                                

"""


class Perro:

    # constructor - propiedades
    def __init__(self):
        self.nombre = ""
        self.tamano = None
        self.color = ""
        self.raza = ""

    # metodos
    def ladrar(self):
        print(f"El perro {nombre_perro} ladra")

    def comer(self):
        print("El perro come")


# Intanciar un objeto
perro = Perro()

# llamar propiedades
nombre_perro = (input("Ingresa nombre: "))
perro.nombre = nombre_perro

tamano_perro = int(input("Digite tamaño: "))
perro.tamano = tamano_perro

print(perro.__dict__)

# llamar metodos
perro.ladrar()
