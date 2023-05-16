# Login

# cuenta ya creada
usuario_logeado = "franco"
usuario_logeado_pass = "saqashjb15"
user_list = []
print("----Menu----")
print("1.Crear cuenta")
print("2.Ingresar")

new_user = int(input("Ingresa un valor: "))
if new_user == 1:
    for i in range(1):
        user = str(input("Ingresa tu nombre de usuario: "))
        passw = str(input("Ingresa tu clave: "))
        passw2 = str(input("Ingresa tu clave nuevamente: "))

    if passw2 == passw:
        print("El usuario fue creado")
        user_list.append(user)
        user_list.append(passw)
        print("----Menu----")
        print("1. Ingresar")
        print("2. Salir")
        new_qs = int(input("Desea ver su cuenta?:"))
        if new_qs == 1:
            ingrese_nombre = str(input("Escriba su usuario creado: "))
            ingrese_clave = str(input("Ingrese su clave: "))
            if ingrese_nombre == user and ingrese_clave == passw:
                print("----Login----")
                print("\nSe logeo con el nombre: ")
                print(f"User: {ingrese_nombre}")
                print(f"Passw: {ingrese_clave}")
                user_list.append(ingrese_nombre)
                user_list.append(ingrese_clave)
                print(user_list)

            elif ingrese_nombre == usuario_logeado and ingrese_clave == usuario_logeado_pass:
                print("Se logeo con el nombre: ")
                print(f"User: {ingrese_nombre}")
                print(f"Passw: {ingrese_clave}")

                user_list.append(ingrese_nombre)
                user_list.append(ingrese_clave)
                print(user_list[0, 1])
            else:
                print("\nVuelva a intentarlo.")
                print("Los usuarios no fueron registrados.\n")

    else:
        print("Clave mal ingresada.")
if new_user == 2:
    user_left = str(input("Ingrese su usuario: "))
    pass_left = str(input("Password: "))

    if (user_left == usuario_logeado and pass_left == usuario_logeado_pass):
        print("Se ha logeado con el nombre de: ")
        print(f"Usuario: {usuario_logeado}")
        print(f"Clave: {usuario_logeado_pass}")
    else:
        print("Usuario no encontrado")
