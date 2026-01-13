def registrar():
    usuario = input("Nuevo usuario: ")
    contraseña = input("Nueva contraseña: ")

    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario}:{contraseña}\n")

    print("Usuario registrado correctamente.")


def iniciar_sesion():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                u, c = linea.strip().split(":")
                if u == usuario and c == contraseña:
                    print("Inicio de sesión exitoso.")
                    return
        print("Usuario o contraseña incorrectos.")
    except FileNotFoundError:
        print("No hay usuarios registrados aún.")


# Menú simple
while True:
    print("\n1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
