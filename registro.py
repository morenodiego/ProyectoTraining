def registrar(): 
    usuario = input("Dime tu nombre de usuario: ")
    contraseña = input("Ponga su contraseña: ")

    # Primero revisamos si el usuario ya existe
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo: 
                nombre_guardado = linea.split(":")[0].strip() 
                if nombre_guardado == usuario:
                    print("Ese usuario ya existe")
                    return
    except FileNotFoundError:
        pass

    # Si no existe, lo guardamos
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario}:{contraseña}\n")

    print("Usuario registrado correctamente")
    
    # Ahora pedimos datos del jugador, prueba con copilot
    print("\nAhora vamos a crear tu perfil de jugador")
    avatar = input("¿Qué avatar quieres? (nombre/descripción): ")
    mascota = input("¿Qué mascota quieres? (nombre/descripción): ")
    peso = int(input("¿Cuál es tu peso en kg? "))
    altura = float(input("¿Cuál es tu altura en metros? "))
    edad = int(input("¿Cuál es tu edad? "))
    
    # Guardar jugador en jugadores.txt
    with open("jugadores.txt", "a") as archivo:
        archivo.write(f"{usuario}:0:1:{avatar}:{mascota}:{peso}:{altura}:{edad}\n")
    
    # Guardar el primer registro de métrica
    from historico import Historico
    from metrica import Metrica
    historico = Historico(usuario)
    metrica = Metrica(peso, altura, edad)
    historico.guardar_registro_metrica(metrica)


def iniciar_sesion(): 
    usuario = input("Dime tu nombre de usuario: ")
    contraseña = input("Ponga su contraseña: ")


    with open("usuarios.txt", "r") as archivo:
        for linea in archivo: 
            nombre_guardado = linea.split(":")[0].strip() 
            contra = linea.split(":")[1].strip() 
            if nombre_guardado == usuario and contra == contraseña: 
                return usuario 
    return ""
