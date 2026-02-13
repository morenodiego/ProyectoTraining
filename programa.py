from registro import registrar,iniciar_sesion
from historico import Historico
from clase_actividad import Ciclismo, Correr, Gimnasio, Actividad
from jugador import Jugador

print("Bienvenido")

menu_inicial = int(input("1.Registrarte\n" \
"2. iniciar sesion\n"\
": " ))

# Cargar histórico y jugador
usuario = None
if menu_inicial == 1: 
    registrar()
    print("\nAhora inicia sesión con tu nueva cuenta")
    usuario = iniciar_sesion()
    if usuario == "":
        print("No existe un usuario así en nuestro sistema")
        exit()

elif menu_inicial == 2: 
    usuario = iniciar_sesion()
    if usuario == "":
        print("No existe un usuario así en nuestro sistema")
        exit()

if usuario:
    historico = Historico(usuario)
    historico.cargar_datos()
    jugador = historico.cargar_jugador(usuario)
    
    # Si no existe el jugador, crearlo ahora
    if jugador is None:
        print("Creando tu perfil de jugador...")
        avatar = input("¿Qué avatar quieres? ")
        mascota = input("¿Qué mascota quieres? ")
        peso = int(input("¿Cuál es tu peso en kg? "))
        altura = float(input("¿Cuál es tu altura en metros? "))
        edad = int(input("¿Cuál es tu edad? "))
        with open("jugadores.txt", "a") as archivo:
            archivo.write(f"{usuario}:0:1:{avatar}:{mascota}:{peso}:{altura}:{edad}\n")
        jugador = historico.cargar_jugador(usuario)
        # Guardar el primer registro de métrica
        historico.guardar_registro_metrica(jugador.metrica)




menu_actividad = int(input
("1.Ciclismo\n" \
"2.Correr\n"\
"3.Gimnasio\n"\
"4.Editar métrica\n"\
": "))

if menu_actividad == 1: 
    hora = int(input("Cuando horas enteras has entrenado : "))
    min = int(input("y cuantos mimnutos: "))
    dur = hora*60 + min
    dist = float(input("Cuantos kilometros enteros: "))
    altmax = int(input("Cuanto ha sido la altmura maxima: "))
    altmin = int(input("Y la minima: "))
    desnivel = altmax - altmin
    act = Ciclismo(dur, "2-1-25",dist,desnivel)
    historico.registrar_actividad(act)
    jugador.ganar_exp(40)
    print(jugador.barra_exp())

elif menu_actividad == 2: 
    hora = int(input("Cuando horas enteras has entrenado : "))
    min = int(input("y cuantos mimnutos: "))
    dur = hora*60 + min
    dist = float(input("Cuantos kilometros enteros: "))
    act = Correr(dur,"2-1-25", dist)
    historico.registrar_actividad(act) 
    jugador.ganar_exp(50)
    print(jugador.barra_exp())


elif menu_actividad == 3: 
    hora = int(input("Cuando horas enteras has entrenado : "))
    min = int(input("y cuantos mimnutos: "))
    dur = hora*60 + min
    
    act = Gimnasio(dur, "2-1-25")  
    act.entrenamiento()  # Llamar al método de entrenamiento
    
    historico.registrar_actividad(act)
    jugador.ganar_exp(50)
    print(jugador.barra_exp())
elif menu_actividad == 4:
    print("\n--- Tu métrica actual ---")
    print(f"Peso: {jugador.metrica.peso} kg")
    print(f"Altura: {jugador.metrica.altura} m")
    print(f"Edad: {jugador.metrica.edad} años")
    print(f"IMC: {jugador.metrica.calcular_imc():.2f}")
    
    modificar = input("\n¿Deseas modificarla? (s/n): ")
    if modificar.lower() == "s":
        jugador.metrica.peso = int(input("Nuevo peso en kg: "))
        jugador.metrica.altura = float(input("Nueva altura en metros: "))
        jugador.metrica.edad = int(input("Nueva edad: "))
        print(f"Métrica actualizada. Nuevo IMC: {jugador.metrica.calcular_imc():.2f}")
        # Guardar el registro de métrica en el historial
        historico.guardar_registro_metrica(jugador.metrica)
    

    


    



historico.guardad_datos()

# Guardar el jugador actualizado
if jugador:
    historico.jugadores.append(jugador)
    historico.guardar_jugadores()