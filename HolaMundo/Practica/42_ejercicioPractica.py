"""
# Creacion de clase
class Usuario:
    pass  # indica que el bloque no realizara ningun tipo de accion


franco = Usuario()
print(franco)

# Atributos de una clase


class User:
    username = "franco"
    email = ""


User.username = "franco 2"
User.email = "franco@gmail.com"
print(User.username)
print(User.email)

# Atributos de instancia
# user1 = User() >> se nombra la clase con una variable
# print(user1.username) >> se muestra el atributo dentro de la clase por la variable nombrada ant.

# 1. Verifica si el atributo existe dentro del objeto
# 2. Verifica si el atributo existe dentro de la clase >> Lee
# 3. Devuelve un error
user1 = User()
user1.username = "Franco"
user1.email = "franco_02@gmail.com"
user1.password = "pass123"  # de esta forma añado un atributo al objeto User()
print(user1.__dict__)  # __dict__ guarda los atributos dentro de un diccionario
"""


class Username:

    def inicializar(self, username, password):  # metodo
        # Añadimos atributos al objeto
        self.username = username
        self.password = password

    def __init__(self, user="", psw=""):
        self.user = user
        self.psw = psw


user1 = Username("Franco", "12345")
user2 = Username("Manuel", "123Pass123")
user3 = Username()  # utiliza los valores por default

# user1.inicializar("Franco", "12345")
# user2.inicializar("Manuel", "123pass")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)