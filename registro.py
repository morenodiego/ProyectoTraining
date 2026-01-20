def registrar(): 
    usuario = input("Dime tu nombre de usuario: ")
    contraseña = input("Ponga su contraseña: ")

    # Primero revisamos si el usuario ya existe
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo: 
            nombre_guardado = linea.split(":")[0] 
            while nombre_guardado == usuario:
                print("Ese usuario ya existe")
                registrar()
                return  # salimos sin registrar

    # Si no existe, lo guardamos
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario}:{contraseña}\n")

    print("Usuario registrado correctamente")


def iniciar_sesion(): 
    usuario = input("Dime tu nombre de usuario: ")
    contraseña = input("Ponga su contraseña: ")


    with open("usuarios.txt", "r") as archivo:
        for linea in archivo: 
            nombre_guardado = linea.split(":")[0] 
            contra = linea.split(":")[1] 
            if nombre_guardado == usuario and contra == contraseña: 
                return usuario 
            else: 
                return ""
