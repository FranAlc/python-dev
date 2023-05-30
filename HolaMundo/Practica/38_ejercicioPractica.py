# Cloures
def saludar(username):
    mensaje = f'Hola {username}'  # variable local

    def mostrar_mensaje():  # Anidada
        print(mensaje)

    return mostrar_mensaje


username = "Franco"
respuesta = saludar(username)
respuesta()  # >> imprime la variable local mensaje , pero aca demuestro una "excepcion" a la regla
