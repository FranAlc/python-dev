class Usuario:
    pass  # indica que el bloque no realizara ningun tipo de accion


franco = Usuario()
print(franco)


class User:
    username = "franco"
    email = ""


User.username = "franco 2"
User.email = "franco@gmail.com"
print(User.username)
print(User.email)
