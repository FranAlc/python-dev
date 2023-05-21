# 13 Realiza un sistema de login: deberá de solicitar el nombre de usuario por teclado y la contraseña

nombre_usuario = "Franco"
passw_usuario = "Ps8229011LlsDptw92nsW"


new_user = input("Crea un usuario: ")
if (new_user != nombre_usuario):
    new_pass_user = input("Crea una clave: ")
    repeat_pass_user = input("Repite la clave: ")
    if (new_pass_user == repeat_pass_user):
        print("\nUsuario creado")
        print(f"User: {new_user}")
        print(f"Pass: {new_pass_user}")
    elif (new_pass_user != repeat_pass_user):
        print(f"Una de las dos contraseñas no coinciden.")
else:
    print("Ingresa otro usuario. User ya existente")
