# Lista de metodos
# Metodos

# Metodo format
nm = "franco"
apl = "galan"
print("{} {}".format(nm.title(), apl.title()))
# Metodo minuscula
nm = "Franco"
print(nm.lower())
# Metodo espacios en blanco -> rstrip()
nm, apl = "Franco", "Galan"
print(nm.rstrip())

# Metodo mayuscula primera letra
nm = "franco"
print(nm.title())
# Concatenacion con el metodo title
nm = "franco"
apl = "galan"
print(f"Hola, {nm.title()} {apl.title()} ")
